//TC: O(Log base 4 N) SC: Log base 4 N
class Solution {
public:
    bool isPowerOfFour(int n) {
        unordered_set<long long> s;
        s.insert(1);
    
        s.insert(4);
        long long mul=4;
        
        for(int i=0; i<15; i++)
        {
            mul*=4;
            s.insert(mul);
        }
        
        return s.count(n)>0;
        
    }
};
