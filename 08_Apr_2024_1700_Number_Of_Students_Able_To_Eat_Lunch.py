class Solution:
    #TC: O(N) SC: O(N)
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
        
