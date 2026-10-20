def helper(self, adj, node, res, visited):
        
    res.append(node)
    visited[node] = True
    
    for i in range(len(adj[node])):
        neighbr = adj[node][i]
        if visited[neighbr] == False:
            self.helper(adj, neighbr, res, visited)
            
    return

def dfs(self, adj):
    
    n = len(adj)
    
    res = []
    visited = [False] * n
    
    self.helper(adj, 0, res, visited)
    
    return res

