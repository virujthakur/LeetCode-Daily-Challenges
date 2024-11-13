#include <ext/pb_ds/assoc_container.hpp> 
#include <ext/pb_ds/tree_policy.hpp> 
using namespace __gnu_pbds; 
  
#define ordered_set tree<int, null_type,less_equal<int>, rb_tree_tag,tree_order_statistics_node_update> 

class Solution {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        ordered_set m;
        long long ans = 0;
        
        for(int i=n-1; i>=0; i--)
        {
            
            int j1 = m.order_of_key(lower - nums[i]);
            int j2 = m.order_of_key(upper - nums[i] + 1);
            
            // cout<< j1<<" "<< j2<<endl;
            ans += (long long)(j2-j1);
            m.insert(nums[i]);
            
        }
        
        return ans;
    }
};
