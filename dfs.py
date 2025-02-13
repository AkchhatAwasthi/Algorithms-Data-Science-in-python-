graph={
    'A': ['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[],}
def dfs_iterative(graph,start):
    visited=set()
    stack=[start]
    result=[]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(reversed(graph[node]))
    return result
print(dfs_iterative(graph,'A'))
