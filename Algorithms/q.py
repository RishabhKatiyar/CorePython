def GetConnectedComponents(_graph):
    #print(_graph)
    vertices = []
    # create graph
    my_graph = {}
    first_node = None
    for g in _graph:
        if first_node is None:
            first_node = g[0]
        if not g[0] in my_graph:
            my_graph[g[0]] = []
        my_graph[g[0]].append(g[1])
        #if not g[1] in my_graph:
        #    my_graph[g[1]] = []
    _visited = set()
    components = []
    _queue = []
    _queue.append(first_node)
    print(_queue)
    while len(_queue):
        vert = _queue.pop(0)
        vertices = my_graph[vert]
        for vertice in vertices:
            #print(vertice)
            if not vertice in _visited:
                _visited.add(vertice)

        print(_visited)

    print(my_graph)
def visit(s):
    pass

print(GetConnectedComponents([['A','B'],['B', 'C'],['D', 'E'],['E', 'F'],['F', 'G'], ["A", "G"]]))
#print(GetConnectedComponents())