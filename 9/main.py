def crc_remainder(data,divisor):
    crc=0
    data=bytearray(data)

    for byte in data:
        crc^=byte
        for _ in range(8):
            if crc&0x80:
                crc=(crc<<1)^divisor
            else:
                crc<<=1

    return crc & 0xFF

def crc_encode(data,divisor):
    remainder=crc_remainder(data,divisor)
    return data+bytes([remainder]) 
def crc_check(data,divisor):
    return crc_remainder(data,divisor)==0

data=b"hello"
divisor=0x9C

encoded= crc_encode(data,divisor)
print(f"Encoded: {encoded}")

corrupted_data=bytearray(encoded)
corrupted_data[2]=0xff

crc_valid=crc_check(corrupted_data,divisor)

if crc_valid:
    print("Data is valid")
else:
    print("Data is corrupted")
