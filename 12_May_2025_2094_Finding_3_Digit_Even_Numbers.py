class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        ans = set()
        for i in range(n):
            for j in range(n):
                if i==j:
                   a continue

                if digits[i]  == 0:
                    continue

                for k in range(n):
                    if j==k or k==i:
                        continue
                      

                    if digits[k]% 2 == 0:
                        # print(i, j, k)
                        # print(digits[i], digits[j], digits[k])
                        # ans.add(int(str(digits[i])+ str(digits[j]) + str(digits[k])))
                        ans.add(digits[i]*100 + digits[j]* 10 + digits[k])

        # print(ans)
        return sorted(list(ans))

                    
