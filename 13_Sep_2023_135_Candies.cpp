//TC: O(N) SC: O(N)
class Solution {
public:
    int candy(vector<int>& ratings) {
        
        int n= ratings.size();
        
        vector<int> L(n,1);
        vector<int> R(n,1);
        
        for(int i=1;i<n;i++)
        {
            if(ratings[i-1] < ratings[i])
                L[i]= L[i-1]+1;
            
            if(ratings[n-1-i+1] < ratings[n-1-i])
               R[n-1-i]= R[n-1-i+1]+1;
                
        }
        
        int sum=0;
        for(int i=0;i<n;i++)
            sum+= max(L[i], R[i]);
        
        return sum;
    }
};