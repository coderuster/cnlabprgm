class Router:
    def __init__(self,graph):
        self.graph = graph
        self.num_nodes=len(graph)

    def dijkstra(self,src):
        visited=[False]*self.num_nodes
        distance=[float('inf')]*self.num_nodes
        distance[src]=0

        for _ in range(self.num_nodes):
            min_dist=float('inf')
            min_index=-1
            for i in range(self.num_nodes):
                if not visited[i] and distance[i]<min_dist:
                    min_dist=distance[i]
                    min_index=i
            visited[min_index]=True

            for v in range(self.num_nodes):
                if not visited[v] and self.graph[min_index][v] and distance[min_index]+self.graph[min_index][v]<distance[v]:
                    distance[v]=distance[min_index]+self.graph[min_index][v]
        return distance

    def shortest_path(self):
        shortest_paths={}
        for i in range(self.num_nodes):
            shortest_paths[i]=self.dijkstra(i)

        return shortest_paths

graph=[ [0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]] 
router=Router(graph)

print(router.shortest_path())
