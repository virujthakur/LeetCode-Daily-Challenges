class Solution:
    #TC: O(N) SC: O(1)
    def closeStrings(self, word1: str, word2: str) -> bool:
        n,m= len(word1), len(word2)
        if n != m:
            return False
        f1, f2= defaultdict(int), defaultdict(int)
        for c1, c2 in zip(word1, word2):
            f1[c1]+=1
            f2[c2]+=1
        
        l1, l2, l3, l4= [], [], [], []
        for k in f1.keys():
            l1.append(k)
            l2.append(f1[k])
        
        for k in f2.keys():
            l3.append(k)
            l4.append(f2[k])
        
        l1.sort()
        l2.sort()
        l3.sort()
        l4.sort()
        
        # print(l1, l2, l3, l4)
        return l1== l3 and l2== l4
