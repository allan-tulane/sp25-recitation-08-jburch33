from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    heap = []
    heappush(heap, (0, 0, source))

    result = {}

    while heap:
      weight_so_far, num_edges_so_far, node = heappop(heap)

      if node in result:
          continue

      result[node] = (weight_so_far, num_edges_so_far)

      for neighbor, edge_weight in graph.get(node, []):
          if neighbor not in result:
              heappush(heap, (weight_so_far + edge_weight, num_edges_so_far + 1, neighbor))

    return result
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    parents = {}
    visited = set()
    queue = deque()

    visited.add(source)
    queue.append(source)

    while queue:
      node = queue.popleft()

      for neighbor in graph.get(node, []):
          if neighbor not in visited:
              parents[neighbor] = node
              visited.add(neighbor)
              queue.append(neighbor)

    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = []
    current = destination

    while current in parents:
      parent = parents[current]
      path.append(parent)
      current = parent

    path.reverse()
    return ''.join(path)
    

