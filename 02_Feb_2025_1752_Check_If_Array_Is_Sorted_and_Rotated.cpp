class Solution {
    //TC: O(NLOGN) SC: O(N)
public:
    bool check(vector<int>& nums) {
        int n= nums.size();
        int idx= -1;
        for(int i=1; i<n; i++)
        {
            if (nums[i] < nums[i-1]){
                idx = i;
            }
        }
        vector<int> temp = nums;
        if (idx == -1){
            sort(temp.begin(), temp.end());
            return temp == nums;
        }

        vector<int> left(nums.begin(), nums.begin() + idx);
        vector<int> right(nums.begin()+idx, nums.end());
        vector<int> l_temp = left;
        sort(l_temp.begin(), l_temp.end());
        vector<int> r_temp = right;
        sort(r_temp.begin(), r_temp.end());


        return l_temp == left and r_temp == right and right.back() <= left.front();
    }
};
