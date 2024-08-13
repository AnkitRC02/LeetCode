class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        results = []

        def backtrack(start, target, path):
            if target == 0:
                results.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        backtrack(0, target, [])
        return results

        