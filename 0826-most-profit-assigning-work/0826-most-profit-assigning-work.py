class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        max_profit = 0
        job_index = 0
        best = 0
        
        for ability in worker:
            while job_index < len(jobs) and jobs[job_index][0] <= ability:
                best = max(best, jobs[job_index][1])
                job_index += 1
            max_profit += best
        
        return max_profit