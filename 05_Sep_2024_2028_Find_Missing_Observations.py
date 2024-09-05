class Solution:
    #TC : O(N) SC: O(1)
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_m = sum(rolls)
        m = len(rolls)
        
        sum_n = mean * (m+n) - sum_m
        
        max_possible_sum_n = 6* n
        min_possible_sum = n
        
        if sum_n > max_possible_sum_n  or sum_n < min_possible_sum:
            return []
        
        answer = [1] * n
        temp_sum = n
        for i in range(n):
            if temp_sum == sum_n:
                break
                
            if temp_sum < sum_n:
                diff = sum_n - temp_sum
                if diff >= 5:
                    answer[i]+= 5
                    temp_sum += 5
                else:
                    answer[i]+= diff
                    temp_sum += diff
                    
        return answer
            
        
        
        
