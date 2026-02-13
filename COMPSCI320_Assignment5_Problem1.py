from collections import deque

class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.g[u].append([v, cap, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])

    def bfs(self, s, t, level):
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, rev in self.g[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] >= 0

    def dfs(self, u, t, f, level, it):
        if u == t:
            return f
        for i in range(it[u], len(self.g[u])):
            it[u] = i
            v, cap, rev = self.g[u][i]
            if cap > 0 and level[v] == level[u] + 1:
                pushed = self.dfs(v, t, min(f, cap), level, it)
                if pushed > 0:
                    self.g[u][i][1] -= pushed
                    self.g[v][rev][1] += pushed
                    return pushed
        return 0

    def maxflow(self, s, t):
        flow = 0
        INF = 10**9
        while True:
            level = [-1] * self.n
            if not self.bfs(s, t, level):
                break
            it = [0] * self.n
            while True:
                pushed = self.dfs(s, t, INF, level, it)
                if pushed == 0:
                    break
                flow += pushed
        return flow


def gomory_hu_tree(n, edges):
    parent = [0] * n
    cutval = [0] * n
    tree = [[] for _ in range(n)]

    for s in range(1, n):
        t = parent[s]

        dinic = Dinic(n)
        for u, v in edges:
            dinic.add_edge(u, v, 1)
            dinic.add_edge(v, u, 1)

        f = dinic.maxflow(s, t)
        cutval[s] = f

        visited = [False] * n
        q = [s]
        visited[s] = True
        while q:
            u = q.pop()
            for v, cap, rev in dinic.g[u]:
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    q.append(v)

        for v in range(s + 1, n):
            if parent[v] == t and visited[v]:
                parent[v] = s

        if visited[parent[t]]:
            parent[s], parent[t] = parent[t], s
            cutval[s], cutval[t] = cutval[t], cutval[s]

    for i in range(1, n):
        tree[i].append((parent[i], cutval[i]))
        tree[parent[i]].append((i, cutval[i]))

    return tree

def solve():
    import sys
    input_data = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(input_data):
            break
        line = input_data[idx].strip()
        idx += 1
        if not line:
            continue
        n = int(line)
        if n == 0:
            break

        adj = [[] for _ in range(n)]
        for i in range(n):
            if idx < len(input_data):
                parts = input_data[idx].strip().split()
                idx += 1
                for p in parts:
                    adj[i].append(int(p))

        edges = set()
        for u in range(n):
            for v in adj[u]:
                if 0 <= v < n:
                    edges.add(tuple(sorted((u, v))))
        edges = list(edges)

        tree = gomory_hu_tree(n, edges)

        best = 0
        for u in range(n):
            for v, w in tree[u]:
                best = max(best, w)

        print(best)


if __name__ == "__main__":
    solve()