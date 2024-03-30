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

data=b"h"
divisor=0x9C
print("data:",bin(ord("h"))[2:])
print("divisor:",bin(divisor)[2:])

encoded= crc_encode(data,divisor)
bin_data=bin(int.from_bytes(encoded,"big"))[2:]
print(f"Encoded: {bin_data}")

corrupted_data=bytearray(encoded)
corrupted_data[0]=0xff

crc_valid=crc_check(corrupted_data,divisor)

if crc_valid:
    print("Data is valid")
else:
    print("Data is corrupted")
