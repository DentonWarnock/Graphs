
# what are the edges: if a descendant/parent
# what are the nodes: numbers/people

# build the graph or write getNeighbors()
# Can do either...

# which algo to go with in this situation???
 # BTF, DFT, BFS, DFS: BFT OR DFT --> both will work
 
# search or traversal?
 # more like a traversal: visit every node possible from your starting node

# BF --> shortest past
# DF --> heads to leaves first

# def earliest_ancestor(ancestors, starting_node, distance=0):    
#     # create a graph
#     graph = {}
#     # iterate over all ancestors, 
#     # add each node to the graph    
#     # add each edge to the graph
#     for parent, child in ancestors:
#         if child not in graph:            
#             graph[child] = [parent]
#         else:
#             graph[child] += [parent]
#     # graph = {child: [parent, parent], child: [parent], ...}      
#     print(graph)
#     # create visited set and add starting node
#     visited = set()
#     visited.add(starting_node)
#     # create a stack and add the starting_node
#     stack = []
#     stack.append([starting_node])
#     path = []
#     # run the traversal - modify it as you go - keep track of the node that's the farthest away    
#     while len(stack) > 0:
#         print(stack)
#         # Dequeue the first PATH
#         current = stack.pop()        
#         child = current[-1]
        
#         if child not in visited:            
#             visited.add(child)  
#             path.append(current)
            
#             for parent in get_parents(ancestors, current):
#                 new_path = list(current)
#                 new_path.append(parent)
#                 stack.append(new_path)
                
#     return path
            
# def get_parents(ancestors, node):
#     parents = set()
#     # loop through ancestors
#     for (parent, child) in ancestors:
#         # if child is node
#         if child == node:
#             # add to list of parents
#             parents.add(parent)
#     return parents


# (parent, child)
def get_parents(ancestors, node):
    parents = []
    for pair in ancestors:
        if pair[1] == node:
            parents.append(pair[0])
    return parents
            
    
    
# Tim guided lecture recursive solution

def dft_recursive(ancestors, node, distance):
    print(node, distance)
    parents = get_parents(ancestors, node)
    
    aged_one = (node, distance)
    
    for parent in parents:
        pair = dft_recursive(ancestors, parent, distance + 1)
        if pair[1] > aged_one[1]:
            aged_one = pair
        
    return aged_one

def earliest_ancestor(ancestors, starting_node, distance=0):   
    aged_one = dft_recursive(ancestors, starting_node, distance)
    
    if aged_one[0] == starting_node:
        return -1
    
    return aged_one[0]
    