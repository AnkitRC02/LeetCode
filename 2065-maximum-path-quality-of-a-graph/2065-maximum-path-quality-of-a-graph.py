
class Solution(object):
    def maximalPathQuality(self, values, edges, maxTime):
        def iter_dfs(values, adj, maxTime):
            lookup, lookup2 = [0]*len(adj), set()
            result = 0
            stk = [(1, (0, maxTime, 0))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, time, total = args
                    lookup[u] += 1
                    if lookup[u] == 1:
                        total += values[u]
                    if not u:
                        result = max(result, total)
                    stk.append((4, (u,)))
                    for v, t in reversed(adj[u]):
                        if (u, v) in lookup2 or time < t:
                            continue
                        stk.append((3, (u, v)))
                        stk.append((1, (v, time-t, total)))
                        stk.append((2, (u, v)))
                elif step == 2:
                    u, v = args
                    lookup2.add((u, v))
                elif step == 3:
                    u, v = args
                    lookup2.remove((u, v))
                elif step == 4:
                    u = args[0]
                    lookup[u] -= 1
            return result

        adj = [[] for _ in xrange(len(values))]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
        return iter_dfs(values, adj, maxTime)