class Solution:
    #TC: O(N) SC: O(1)
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens, twenties = 0,0,0
        for b in bills:
            if b == 5:
                fives+=1
                continue
                
            elif b== 10:
                tens+=1
                if fives ==0:
                    return False
                fives -=1
                
            else:
                twenties+=1
                if tens > 0 and fives > 0:
                    tens-=1
                    fives-=1
                    continue
                elif fives >=3:
                    fives-=3
                    continue
                else:
                    return False
                
        return True
                
