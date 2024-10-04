class Solution:
    #TC: O(NLOGN) SC: O(1)
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j = 0, len(skill)-1
        prev = -1
        ans = 0
        while i<j:
            if prev!=-1 and prev != skill[i]+ skill[j]:
                return -1
            
            ans+= skill[i]* skill[j]
            prev = skill[i] + skill[j]
            i+=1
            j-=1
            
        return ans
