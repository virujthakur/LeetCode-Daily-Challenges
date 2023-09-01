//TC: O(NLOGN) SC: O(1)

class Solution {
public:
    vector<int> countBits(int n) {
        
        vector<int> ans;
        
        for(int i=0;i<=n;i++)
        {
            int count=0;
            int num=i;
            while(num>0)
            {
                int rem= num%2;
                if(rem)
                    count++;
                num/=2;
            }
            
            ans.push_back(count);
        }
        
        return ans;
        
    }