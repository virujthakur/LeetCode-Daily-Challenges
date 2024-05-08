class Solution:
    #TC: O(NLOGN) SC: O(N)
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score= [(score[_], _) for _ in range(len(score))]
        score.sort(reverse = True)
        ans = ['']* len(score)
        for i,s in enumerate(score):
            if i==0:
                ans[s[1]]= 'Gold Medal'
            elif i ==1:
                ans[s[1]]= 'Silver Medal'
            elif i== 2:
                ans[s[1]]= 'Bronze Medal'
            else:
                ans[s[1]]= str(i+1)
        
        return ans
