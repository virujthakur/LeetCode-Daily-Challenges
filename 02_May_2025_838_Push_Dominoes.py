class Solution:
    #TC: O(2N) SC: O(1)
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        dominoes = [c for c in dominoes]
        n = len(dominoes)

        i = 0
        for j in range(n):
            if dominoes[j] == 'L':
                if dominoes[i] == 'L':
                    for k in range(i, j+1):
                        dominoes[k] = 'L'
                else:
                    half = (j-i+1) // 2
                    for k in range(i, i+half):
                        dominoes[k] = 'R'
                    
                    for k in range(j, j-half, -1):
                        dominoes[k] = 'L'
                i= j
            elif dominoes[j] == 'R':
                if dominoes[i] == 'R':
                    for k in range(i, j+1):
                        dominoes[k] = 'R'
                i= j

        
        return ''.join(dominoes)[1:-1]
