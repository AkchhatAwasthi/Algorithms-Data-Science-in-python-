def iterative_deepening_search(start, goal, successors):
    def depth_limited_search(state, depth, path):
        if state == goal:
            return path, len(path) - 1 
        if depth == 0:
            return None, None
        for successor in successors(state):
            result, result_depth = depth_limited_search(successor, depth - 1, path + [successor])
            if result is not None:
                return result, result_depth  
        return None, None  

    depth = 0
    while True:
        result, result_depth = depth_limited_search(start, depth, [start])
        if result is not None:
            return result, result_depth 
        depth += 1  

def successors(state):
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [], 'E': [], 'F': [], 'G': []
    }
    return graph[state]


start = 'A'
goal = 'G'


solution_path, depth_found = iterative_deepening_search(start, goal, successors)
if solution_path:
    print("Solution path:", solution_path)
    print("Depth found:", depth_found)
else:
    print("Not found")
