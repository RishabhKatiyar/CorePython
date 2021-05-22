# cat SourceToDestinationPath | python SourceToDestinationPath.py

number_of_nodes = int(input())

nodes = []

for _ in range(number_of_nodes):
    nodes.append(int(input()))

number_of_edges = int(input())

edges = []
for _ in range(number_of_edges):
    edge = input().split(" ")
    edge_tuple = [int(edge[0]), int(edge[1]), 0]
    edges.append(edge_tuple)

source = int(input())
destination = int(input())

'''
print('Entered values are..')
print(number_of_nodes)
for i in range(number_of_edges):
    print(nodes[i])
print(number_of_edges)
for i in range(number_of_edges):
    print(f'{edges[i][0]} {edges[i][1]}')
print(source)
print(destination)
'''

def find_path(source, destination, final_destination, edges):
    print(f'{source} -> {destination}, {final_destination}')
    if destination == final_destination:
        print('node reached')
        return 1

    for edge in edges:
        if destination == edge[0] and edge[2] == 0:
            # print(f'{edge[1]}, {final_destination}')
            edge[2] = 1
            return find_path(edge[0], edge[1], final_destination, edges)

    return 0

for edge in edges:
    if source == edge[0]:
        node = edge[1]
        edge[2] = 1
        print(find_path(edge[0], edge[1], destination, edges))
        break
        