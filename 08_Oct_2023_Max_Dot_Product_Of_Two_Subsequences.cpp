class Solution {
public:
    
    vector<vector<long long>> dp;
    long long recur(vector<int>& nums1, vector<int>& nums2, int i, int j)
    {
        int n= nums1.size();
        int m= nums2.size();
        
        if(i==n || j==m) return 0;
        
        if(dp[i][j]!=-1) return dp[i][j];
        
        long long result= -1e9;
        
        result = max(result, nums1[i]* nums2[j] + recur(nums1, nums2, i+1, j+1));
        
        result= max(result, recur(nums1, nums2, i, j+1));
        
        result= max(result, recur(nums1, nums2, i+1, j));
        
        return dp[i][j]= result;
    }
    
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        
        int n= nums1.size();
        int m= nums2.size();
        dp.resize(n, vector<long long>(m,-1));
        
        int res = recur(nums1, nums2, 0, 0);
        
        if(res==0)
        {
            int temp= -1e9;
            for(int i=0;i<n;i++)
            {
                for(int j=0; j<m; j++)
                {
                    temp= max(temp, nums1[i]* nums2[j]);
                }
            }
            
            return temp;
        }
        
        
        return res;
    }
};
