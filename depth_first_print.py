# def depthFirstPrint(graph,src): # iterative
#     # sourcery skip: for-append-to-extend, simplify-generator
#     stack = [src]
#     while stack:
#         current = stack.pop()
#         print(current)
#         for neighbor in graph[current]:
#             stack.append(neighbor)
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


def depthFirstPrint(graph, src): # recursive
    print(src)
    for neighbor in graph[src]:
        depthFirstPrint(graph,neighbor)


depthFirstPrint(graph,'a')
