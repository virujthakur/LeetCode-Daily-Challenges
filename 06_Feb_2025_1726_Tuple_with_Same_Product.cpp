class Solution {
public:
    //TC: O(N^2) SC: O(N^2)
    int tupleSameProduct(vector<int>& nums) {
        int n= nums.size();
        unordered_map<int,int> f;
        for(int i=0; i<n; i++)
        {
            for(int j=i+1; j<n; j++)
            {
                if (nums[i] != nums[j])
                    f[nums[i]* nums[j]] +=1;

            }
        }

        int ans = 0;
        for(auto x: f)
        {
            if(x.second >= 2)
            {
                ans+= (x.second)* (x.second-1) * 4;
            }
        }

        return ans;
        
    }
};
