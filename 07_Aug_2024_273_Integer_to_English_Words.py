class Solution:
    #TC: O(3* 6) SC: O(10)
    def numberToWords(self, num: int) -> str:
        l= ["One", "Ten", "Hundred", "Thousand", "Million", "Billion"]
        l.reverse()
        
        tens = ["Zero", "One", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        
        div2 = [100, 10, 1]
        
        div= [1, 10, 100, 1000, 1000000, 1000000000]
        div.reverse()
        
        if num == 0:
            return "Zero"
        
        ans = ''
        for i, d in enumerate(div):
            q= num // d
            
            if q > 0:
                # print(q)
                
                if d==10:
                    if q==1:
                        nextq = num % 10
                        ans += teens[nextq] + ' '
                        break
                    else:
                        ans+= tens[q] + ' '
                        num -= q * d
                        continue
                
                tempq = q
                strq = ''
                
                for j, d2 in enumerate(div2):
                    q2 = tempq // d2
                    
                    if q2 > 0:
                        if d2 == 10:
                            if q2 ==1:
                                nextq2 = tempq % 10
                                strq += teens[nextq2] + ' '
                                break
                            else:
                                strq+= tens[q2] +' '
                                tempq-= q2* d2
                                continue
                        
                        if d2 == 100:
                            strq += digits[q2] + ' ' + 'Hundred' + ' '
                        else:
                            strq += digits[q2] + ' '
                    
                    tempq-= q2* div2[j]
                
                strq = strq[: -1]
                
                if d==1:
                    ans += strq + ' '
                else:
                    ans += strq + ' ' + l[i] + ' '
            
            num -= q* d
              
        
        return ans[: -1]
                
        
        
        
        
