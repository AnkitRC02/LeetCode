class Solution(object):
    def numTeams(self, rating):
        n = len(rating)
        count = 0
        
        for j in range(1, n-1):
            less_left = less_right = more_left = more_right = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    less_left += 1
                if rating[i] > rating[j]:
                    more_left += 1
            
            for k in range(j+1, n):
                if rating[k] < rating[j]:
                    less_right += 1
                if rating[k] > rating[j]:
                    more_right += 1
            
            count += less_left * more_right + more_left * less_right
        
        return count

        