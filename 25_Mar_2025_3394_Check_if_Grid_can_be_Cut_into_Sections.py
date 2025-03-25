class Solution:
    # TC: O(N) SC: O(1)
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        rectangles.sort(key=lambda x: x[1])
        rectangles_copy = copy.copy(rectangles)
        n = len(rectangles)
        # print(rectangles)

        i =0
        cnt = 0
        for j in range(n):
            stxj, styj, enxj, enyj = rectangles[j]
            stxi, styi, enxi, enyi = rectangles[i]
            # print(styj, enyi)

            if styj < enyi:
                enxi = max(enxj, enxi)
                enyi = max(enyj, enyi)
                stxi = min(stxj, stxi)
                rectangles[i] = [stxi, styi, enxi, enyi]
            else:
                cnt+=1
                i= j

        if cnt >=2:
            return True

        cnt = 0
        i = 0
        
        # print(rectangles_copy)
        rectangles_copy.sort()
        # print(rectangles_copy)
        for j in range(n):
            stxj, styj, enxj, enyj = rectangles_copy[j]
            stxi, styi, enxi, enyi = rectangles_copy[i]
            print(styj, enyi)

            if stxj < enxi:
                enxi = max(enxj, enxi)
                enyi = max(enyj, enyi)
                styi = min(styj, styi)
                rectangles_copy[i] = [stxi, styi, enxi, enyi]
            else:
                cnt+=1
                i= j

        # print(rectangles_copy)
        
        if cnt >=2:
            return True


        return False
