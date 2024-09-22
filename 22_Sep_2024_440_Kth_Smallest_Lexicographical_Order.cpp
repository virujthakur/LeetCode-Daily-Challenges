class Solution {
public:
    //TC: O(LOG^2(N)) SC: O(1)
    int calc_steps(long curr, long next, long n)
    {
        int steps=0;
        while(curr<=n)
        {
            steps+= min(next-curr, n-curr+1);
            curr*=10;
            next*=10;
        }
        
        return steps;
    }
    
    int findKthNumber(int n, int k) {
        
        int curr=1;
        k--;
        while(k>0)
        {
            int next= curr+1;
            int steps= calc_steps(curr,next,n);
            
            if(steps<=k)
            {
                k-=steps;
                curr++;
            }
            else
            {
                k--;
                curr*=10;
            }
        }
        
        return curr;
    }
};
