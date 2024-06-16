class Solution {
public:
    //TC; O(N+ LOG(N)) SC: O(1)
    int minPatches(vector<int>& nums, int n) {
        
        long long miss = 1 ;
        int i = 0 ;
        int ans = 0 ;
        
        while(miss <= n)
        {
            if(i< nums.size() and nums[i] <= miss)
            {
                miss = miss + nums[i] ;
                i++;
            }
            else
            {
                ans++;
                miss = miss + miss ;
            }
        }
        
        return ans ;
    }
};
