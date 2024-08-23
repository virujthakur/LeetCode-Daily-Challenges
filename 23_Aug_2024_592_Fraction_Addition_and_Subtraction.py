class Solution:
    #TC: O(N) + O(LOG(10^10)) SC: O(N)
    def fractionAddition(self, expression: str) -> str:
        fractions = []
        isAdded = []
        fraction = ''
        
        if expression[0]!= '-':
            isAdded.append(True)
        
        for c in expression:
            if c== '+':
                fractions.append(fraction)
                isAdded.append(True)
                fraction = ''
                continue
            
            if c== '-':
                if fraction != '':
                    fractions.append(fraction)
                isAdded.append(False)
                fraction = ''
                continue
                
            fraction += c
            
        fractions.append(fraction)
        
        # print(fractions)
        
        numes , denos = [], []
        for f in fractions:
            nume, deno = f.split('/')
            numes.append(int(nume))
            denos.append(int(deno))
            
        # print(numes, denos)
        
        lcm= math.prod(denos)
        for i in range(len(numes)):
            numes[i] = numes[i] * (lcm // denos[i])
            
        res = 0
        for i in range(len(numes)):
            if isAdded[i]:
                res+= numes[i]
            else:
                res-= numes[i]
                
        while math.gcd(res, lcm)!= 1:
            g = math.gcd(res, lcm)
            res //= g
            lcm //= g
        
        # print(res, lcm)
        
        return str(res) + '/' + str(lcm)
