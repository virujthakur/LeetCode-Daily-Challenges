//TC : O(N) SC : O(1)
class Solution {
public:
    long long minimumReplacement(vector<int>& nums) {
        
        int n= nums.size();
        long long ops=0;
        
        for(int i= n-2; i>=0; i--)
        {
            if(nums[i] > nums[i+1])
            {
                long long parts=  ceil(nums[i]/(double)nums[i+1]);
                ops+= parts-1;
                nums[i] = nums[i]/parts;
            }
        }
        
        return ops;
        
    }
};