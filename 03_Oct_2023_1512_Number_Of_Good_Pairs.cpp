//TC: O(N) SC: O(N)
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int n= nums.size();
        unordered_map<int,int> f;
        
        int ans=0;
        for(int i=n-1; i>=0; i--)
        {
            f[nums[i]]++;
            ans+= f[nums[i]]-1;
            

        }
        
        return ans;
            
    }
};
