from collections import deque
import sys

class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        # to, capacity, index_of_reverse_edge_in_g[v]
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
        INF_FLOW = 10**9  # just a large bound for DFS push
        while True:
            level = [-1] * self.n
            if not self.bfs(s, t, level):
                break
            it = [0] * self.n
            while True:
                pushed = self.dfs(s, t, INF_FLOW, level, it)
                if pushed == 0:
                    break
                flow += pushed
        return flow

def max_vertex_disjoint_between(n, edges, a, b):
    """
    Return max # vertex-disjoint paths between a and b in the undirected graph given by edges.
    Uses node-splitting: for each original node i:
      i_in = i
      i_out = i + n
    i_in -> i_out has capacity 1 (except endpoints a,b have INF)
    For each undirected edge (u,v), add u_out -> v_in and v_out -> u_in with capacity INF.
    """
    TOT = 2 * n
    dinic = Dinic(TOT)
    INF = n  # safe upper bound on number of disjoint paths

    # node capacities
    for i in range(n):
        cap = INF if i == a or i == b else 1
        dinic.add_edge(i, i + n, cap)

    # undirected edges as two directed INF arcs
    for (u, v) in edges:
        if u == v:
            continue
        dinic.add_edge(u + n, v, INF)
        dinic.add_edge(v + n, u, INF)

    source = a + n  # a_out
    sink = b        # b_in
    return dinic.maxflow(source, sink)

def solve():
    data = sys.stdin.read().splitlines()
    idx = 0
    outputs = []
    while idx < len(data):
        line = data[idx].strip()
        idx += 1
        if not line:
            continue
        try:
            n = int(line)
        except:
            continue
        if n == 0:
            break

        adj = [[] for _ in range(n)]
        # read n adjacency lines (may be empty)
        for i in range(n):
            if idx < len(data):
                parts = data[idx].strip().split()
                idx += 1
                for p in parts:
                    if p != '':
                        adj[i].append(int(p))

        edges = set()
        for u in range(n):
            for v in adj[u]:
                if 0 <= v < n:
                    edges.add(tuple(sorted((u, v))))
        edges = [e for e in edges if e[0] != e[1]]

        best = 0
        # try every unordered pair (u, v)
        for u in range(n):
            # small optimization: if best already equals n (max possible), stop
            if best >= n:
                break
            for v in range(u + 1, n):
                # another small optimization: if best >= n, break
                if best >= n:
                    break
                val = max_vertex_disjoint_between(n, edges, u, v)
                if val > best:
                    best = val

        outputs.append(str(best))

    sys.stdout.write("\n".join(outputs))

if __name__ == "__main__":
    solve()