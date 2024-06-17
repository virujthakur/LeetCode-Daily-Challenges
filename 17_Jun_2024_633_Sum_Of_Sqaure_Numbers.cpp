class Solution {
public:
    //TC: O(SQRT(N)) SC: O(1)
    bool judgeSquareSum(int c) {
        
        for(long long i=0; i*i <= c; i++)
        {
            long long a= i;
            long long b= sqrt(c- i*i);
            
            if (a*a + b*b == c)
                return true;
        }
        
        return false;
    }
};
