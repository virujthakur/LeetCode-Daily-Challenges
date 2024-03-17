class Solution:
    #TC: O(NLOGN) SC: O(1)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        n= len(intervals)
        # print(intervals)
        ans = []
        
        i= 0
        while i < n:
            x1, y1= intervals[i]
            j= i+1
            while j< n:
                x2, y2= intervals[j]
                if x2 <= y1:
                    y1= max(y1, y2)
                    j+=1
                else:
                    ans.append([x1, y1])
                    break
            else:
                ans.append([x1, y1])
                
            i=j
        return ans
