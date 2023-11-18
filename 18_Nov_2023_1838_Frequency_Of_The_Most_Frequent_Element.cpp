class Solution {
public:
    //TC: (NLOGN) SC: O(N)
    bool isValid(int mid, vector<int>& nums, int k, vector<long long>& prefix, int j, int i)
    {
        int n= nums.size();
        long long expectedSum=  (long long)nums[i]* mid;
        long long psum=0;
        if(i-1-mid >= 0)
            psum= prefix[i-1] - prefix[i-1- mid];
        else
            psum= prefix[i-1];
        
        long long opsReqd= expectedSum - psum;
        // if(j== 72)
            // cout<< expectedSum << " "<< psum<<" "<< opsReqd<<endl;
        
        return opsReqd <= k;
        
    }
    int maxFrequency(vector<int>& nums, int k) {
        int n= nums.size();
        sort(nums.begin(), nums.end());
        vector<long long> prefix(n);
        long long sum=0;
        for(int i=0; i<n; i++)
        {
            sum+= nums[i];
            prefix[i]= sum;
        }
        
        int i=0;
        int j=1;
        int res= 1;
        
        
        while(i<n)
        {
            while(j<n && nums[j]== nums[i])
            j++;
            
            // cout<< i <<" " << j<<endl;
            int f= j-i;
            int l= 1;
            int h= i;
            int ans=0;
            
            while(l<=h)
            {
                int mid= l+ (h-l)/2;
                
                if(isValid(mid, nums,k, prefix, j, i))
                {
                    ans= max(ans,mid);
                    l= mid+1;
                }
                else
                    h= mid-1;
            }
            
            // cout<< f <<" "<< ans<<" " << f+ ans<<" "<<nums[i]<<endl;
            
            res= max(res, f+ ans);
            
            i=j;
        }
        
        return res;
        
    }
};
