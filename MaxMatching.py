import sys
from collections import deque

def bfs():
    queue = deque()
    for u in range(order):
        if match_u[u] == -1:  # Unmatched vertex on the left side
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('inf')
    dist[-1] = float('inf')  # Distance for unmatched vertex on the right

    while queue:
        u = queue.popleft()
        if dist[u] < dist[-1]:  # If we haven't reached the unmatched vertex
            for v in adj[u]:
                if dist[match_v[v]] == float('inf'): 
                    dist[match_v[v]-1] = dist[u] + 1
                    queue.append(match_v[v])
    return dist[-1] != float('inf')

def dfs(u):
    if u != -1:
        for v in adj[u]:
            if dist[match_v[v]] == dist[u] + 1 and dfs(match_v[v]):
                match_u[u] = v
                match_v[v] = u
                return True
        dist[u] = float('inf')  # Mark as unreachable
        return False
    return True

def hopcroft_karp():
    match_count = 0
    while bfs():  # Find all augmenting paths
        for u in range(order):
            if match_u[u] == -1 and dfs(u):  # If vertex u is unmatched
                match_count += 1
    return match_count

# Input reading
while True:
    try:
        order = int(sys.stdin.readline().strip())
        if order == 0:
            break
    except EOFError:
        break

    adj = [[] for _ in range(order)]
    
    # Read the adjacency lists
    for u in range(order):
        adj[u] = list(map(int, sys.stdin.readline().strip().split()))
    
    match_u = [-1] * order  # Matches for U
    match_v = [-1] * order  # Matches for V
    dist = [-1] * (order + 1)  # Distances for BFS
    
    max_matching = hopcroft_karp()
    print(max_matching)