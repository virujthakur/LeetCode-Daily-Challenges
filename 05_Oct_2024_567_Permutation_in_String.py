class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = [0]* 26
        for c in s1:
            cnt[ord(c)- ord('a')]+=1
            
        def isValid():
            for i in range(26):
                if cnt2[i] != cnt[i]:
                    return False
                
            return True
        
        i = 0
        cnt2 = [0]* 26
        for j in range(len(s2)):
            
            cnt2[ord(s2[j])- ord('a')]+=1
            
            while i<=j and cnt2[ord(s2[j])- ord('a')] > cnt[ord(s2[j])- ord('a')]:
                cnt2[ord(s2[i])- ord('a')]-=1
                i+=1
            
            if isValid():
                return True
            
        return False
