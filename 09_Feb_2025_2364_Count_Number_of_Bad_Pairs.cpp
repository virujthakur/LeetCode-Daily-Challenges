class Solution {
public:
    //TC: O(NLOGN) SC: O(1)
    long long countBadPairs(vector<int>& nums) {
        int n= nums.size();
        for(int i=0; i<n; i++)
            nums[i]-=i;

        long long good = 0;
        unordered_map<int,int> f;
        for(int i=n-1; i>=0; i--)
        {
            good += f[nums[i]];
            f[nums[i]] +=1;
        }

        return ((long long)n* (n-1))/2 - good;
    }
};
