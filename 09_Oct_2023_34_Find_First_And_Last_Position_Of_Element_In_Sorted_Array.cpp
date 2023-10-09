class Solution {
public:
    //TC: O(LOGN) SC: O(1)
    vector<int> searchRange(vector<int>& nums, int target) {
        
        int f= lower_bound(nums.begin(), nums.end(), target)- nums.begin();
        int l= upper_bound(nums.begin(), nums.end(), target)- nums.begin();
        
        if(f==l)
            return {-1,-1};
        else
            return {f,l-1};
        
    }
};
