class Solution {
public:
    //TC : O(N) + LOG(M)  SC:O(N)
    int M= 1e9+7;
    
    long long fast_exp(long long a, long long b)
    {
        long long result=1;
        while(b>0)
        {
            if(b%2)
            {
                result= (result%M * a% M) %M;
                b--;
            }
            else
            {
                a= (a* a)% M;
                b/=2;
            }
        }
        return result;
    }
    
    int countOrders(int n) {
        
        vector<long long> fact(2*n+1);
        fact[0]=1;
        fact[1]=1;
        
        for(int i=2;i<2*n+1;i++)
            fact[i]= (fact[i-1]* i) % M;
        
        
        return fact[2*n] * fast_exp(fast_exp(2,n),M-2) % M;
        
    }
};