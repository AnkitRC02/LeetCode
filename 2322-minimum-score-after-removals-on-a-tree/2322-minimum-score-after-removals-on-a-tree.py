class Solution(object):
    def minimumScore(self, nums, edges):
        def is_ancestor(a, b):
            return left[a] <= left[b] and right[b] <= right[a]

        def iter_dfs():
            cnt = 0
            left = [0]*len(nums)
            right = [0]*len(nums)
            stk = [(1, (0, -1))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p = args
                    left[u] = cnt
                    cnt += 1
                    stk.append((2, (u, p)))
                    for v in adj[u]:
                        if v == p:
                            continue
                        stk.append((1, (v, u)))
                elif step == 2:
                    u, p = args
                    for v in adj[u]:
                        if v == p:
                            continue
                        nums[u] ^= nums[v]
                    right[u] = cnt
            return left, right
                
        adj = [[] for _ in xrange(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        left, right = iter_dfs()
        result = float("inf")
        for i in xrange(1, len(nums)):
            for j in xrange(i+1, len(nums)):
                if is_ancestor(i, j):
                    a, b, c = nums[0]^nums[i], nums[i]^nums[j], nums[j]
                elif is_ancestor(j, i):
                    a, b, c = nums[0]^nums[j], nums[j]^nums[i], nums[i]
                else:
                    a, b, c = nums[0]^nums[i]^nums[j], nums[i], nums[j]
                result = min(result, max(a, b, c)-min(a, b, c))
        return result