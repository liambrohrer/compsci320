from collections import defaultdict, deque

def bfs(start, graph):
    visited = set()
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return visited

def max_bipartite_matching(laptops, compat):
    matchR = {}
    
    def dfs(u, seen):
        for v in compat[u]:
            if v not in seen:
                seen.add(v)
                if v not in matchR or dfs(matchR[v], seen):
                    matchR[v] = u
                    return True
        return False
    
    result = 0
    for u in laptops:
        if dfs(u, set()):
            result += 1
    return result

def solve():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        outlets = [input().strip() for _ in range(n)]

        m = int(input().strip())
        laptops = [input().strip() for _ in range(m)]

        k = int(input().strip())
        adapters = defaultdict(list)
        for _ in range(k):
            a, b = input().split()
            adapters[a].append(b)

        all_plugs = set(outlets + laptops + list(adapters.keys()) + [b for v in adapters.values() for b in v])
        reachable = {}
        for plug in all_plugs:
            reachable[plug] = bfs(plug, adapters)
            reachable[plug].add(plug)

        compat = defaultdict(list)
        for i, lplug in enumerate(laptops):
            for j, oplug in enumerate(outlets):
                if oplug in reachable[lplug]:
                    compat[i].append(j)

        powered = max_bipartite_matching(range(m), compat)
        print(m - powered)

if __name__ == "__main__":
    solve()