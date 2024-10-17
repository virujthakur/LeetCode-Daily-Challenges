class Solution:
    #TC: O(1) SC: O(1)
    def maximumSwap(self, num: int) -> int:
        temp = list(str(num))
        temp2 = list(str(num))
        temp.sort(reverse= True)
        
        # print(temp2, temp)
        
        n = len(temp)
        for i in range(n):
            if temp2[i]== temp[i]:
                continue
            else:
                oc = temp2[i]
                temp2[i] = temp[i]
                j = n-1
                while j> i:
                    if temp2[j] == temp[i]:
                        temp2[j]= oc
                        break
                    j-=1
                break
                    
        return int(str(''.join(temp2)))
