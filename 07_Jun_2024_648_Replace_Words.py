class Solution:
    #TC: O(Len(Sentence)) SC: O(Len(words))
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        words = sentence.split(' ')
        n= len(words)
        newwords= [''] * n
        
        def recur(idx):
            if idx == n:
                return
            
            sub = ''
            for j in range(len(words[idx])):
                sub += words[idx][j]
                # print(sub)
                if sub in dictionary:
                    newwords[idx] = sub
                    recur(idx+1)
                    return
            
            newwords[idx]= words[idx]
            recur(idx+1)
                    
        recur(0)
        return ' '.join(newwords)
                    
                    
                
