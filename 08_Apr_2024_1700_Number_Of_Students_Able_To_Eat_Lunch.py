class Solution:
    #TC: O(N^2) SC: O(N) SIMULATION
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i,j = 0,0
        cnt = 0
        while i < len(students):
            print(i,cnt)
            if cnt > (2* (len(sandwiches)- j)):
                break
            
            if students[i] == sandwiches[j]:
                j+=1
                cnt = 0
            else:
                students.append(students[i])
                cnt+=1
            i+=1
            
        return len(sandwiches)- j
    
    
    #TC: O(N) SC: O(1) COUNTING
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt0, cnt1 = 0,0
        for s in students:
            if s: cnt1+=1
            else: cnt0+=1
                
        for s in sandwiches:
            if s and cnt1:
                cnt1-=1
            elif not s and cnt0:
                cnt0-=1
            else:
                break
                
        return cnt0+ cnt1
        
        
