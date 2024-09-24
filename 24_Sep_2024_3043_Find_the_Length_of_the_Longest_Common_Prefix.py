class Solution:
    #TC: O(8N) SC: O(1)
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        class TrieNode:
            def __init__(self):
                self.val = -1
                self.children = [None]* 10
                self.isEnd = False
                
        class Trie:
            def __init__(self, root):
                self.root = root
                
            def insert(self, num):
                ptr = self.root
                for c in num:
                    if ptr.children[int(c)] == None:
                        newNode= TrieNode()
                        ptr.children[int(c)]= newNode
                        
                    ptr= ptr.children[int(c)]
                    
                ptr.isEnd = True
                
            def longestPrefix(self, num):
                ptr= self.root
                ans = 0
                
                for c in num:
                    if ptr.children[int(c)]== None:
                        return ans
                    
                    ptr= ptr.children[int(c)]
                    ans+=1
                    
                return ans
        
        root1 = TrieNode()
        t1 = Trie(root1)
        root2 = TrieNode()
        t2 = Trie(root2)
        
        ans= 0
        for num in arr1:
            t1.insert(str(num))
            
        for num in arr2:
            t2.insert(str(num))
            
        for num in arr2:
            ans= max(ans, t1.longestPrefix(str(num)))
            
        for num in arr1:
            ans= max(ans, t2.longestPrefix(str(num)))
            
        return ans
        
            
            
                    
