#1. has path
# Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst).
#  The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

def has_path(graph, src, dst): # recursive function to check if there is a path between two nodes in a graph using DFS algorithm.
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True
    
  return False

# n = number of nodes
# e = number edges
# Time: O(e)
# Space: O(n)


# from collections import deque

# print("this function is not working!!!")

# def has_path(graph, src, dst): # iterative function to check if there is a path between two nodes in a graph using BFS algorithm.
#   queue = deque([ src ])
#     
#   while queue:
#     current = queue.popleft()
#         
#     if current == dst:
#       return True
    
#     for neighbor in graph[current]:
#       queue.append(neighbor)
    
#   return False

# n = number of nodes
# e = number edges
# Time: O(e)
# Space: O(n)



# if __name__ == '__main__':

  # test_00:
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'f', 'k') # True

# test_01:
# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }

# has_path(graph, 'f', 'j') # False

# # test_02:
# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }

# has_path(graph, 'i', 'h') # True
# # test_03:
# graph = {
#   'v': ['x', 'w'],
#   'w': [],
#   'x': [],
#   'y': ['z'],
#   'z': [],  
# }

# has_path(graph, 'v', 'w') # True
# # test_04:
# graph = {
#   'v': ['x', 'w'],
#   'w': [],
#   'x': [],
#   'y': ['z'],
#   'z': [],  
# }

# has_path(graph, 'v', 'z') # False