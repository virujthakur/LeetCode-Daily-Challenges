class Solution {
public:
    //TC: O(N) SC: O(1)
    vector<int> sortArrayByParity(vector<int>& nums) {
        
        int n= nums.size();
        int i=0;
        int j=n-1;
        
        while(i<j)
        {
            if(nums[i]%2 && !(nums[j]%2))
            {
                swap(nums[i], nums[j]);
                i++;
                j--;
            }
            else if(nums[i]%2 && nums[j]%2)
            {
                j--;
            }
            else if(!(nums[i]%2) && !(nums[j]%2))
            {
                i++;
            }
            else
            {
                i++;
                j--;
            }
        }
        
        return nums;
        
    }
};
