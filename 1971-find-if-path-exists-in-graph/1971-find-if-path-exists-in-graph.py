import collections

class Solution(object):
    def validPath(self, n, edges, start, end):
        def bi_bfs(adj, start, target):
            left, right = {start}, {target}
            lookup = set()
            steps = 0
            while left:
                for pos in left:
                    lookup.add(pos)
                new_left = set()
                for pos in left:
                    if pos in right: 
                        return steps
                    for nei in adj[pos]:
                        if nei in lookup:
                            continue
                        new_left.add(nei)
                left = new_left
                steps += 1
                if len(left) > len(right): 
                    left, right = right, left
            return -1

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return bi_bfs(adj, start, end) >= 0