#2. Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
# The function should return a boolean indicating whether or not there exists a path between node_A and node_B.

def undirected_path(edges, node_A, node_B): # O(n) time | O(n) space 
  graph = build_graph(edges)
  return has_path(graph, node_A, node_B, set())

def build_graph(edges):
  graph = {}
  
  for edge in edges:
    a, b = edge
    
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
      
    graph[a].append(b)
    graph[b].append(a)
    
  return graph
    
def has_path(graph, src, dst, visited):
  if src == dst:
    return True
  
  if src in visited:
    return False
  
  visited.add(src)
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited) == True:
      return True
    
  return False


# n = number of nodes
# e = number edges
# Time: O(e)
# Space: O(n)

# test_00:
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'j', 'm') # -> True
# test_01:
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'm', 'j') # -> True
# test_02:
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'l', 'j') # -> True
# test_03:
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'k', 'o') # -> False
# test_04:
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'i', 'o') # -> False
# test_05:
edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]


undirected_path(edges, 'a', 'b') # -> True
# test_06:
edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

undirected_path(edges, 'a', 'c') # -> True
# test_07:
edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

undirected_path(edges, 'r', 't') # -> True
# test_08:
edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]

undirected_path(edges, 'r', 'b') # -> False
# test_09:
edges = [
  ('s', 'r'),
  ('t', 'q'),
  ('q', 'r'),
];

undirected_path(edges, 'r', 't'); # -> True