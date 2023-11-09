//TC: O(N) SC: O(1)
class Solution {
public:
    int countHomogenous(string s) {
        int n= s.size();
        
        int i=0;
        int j=0;
        long long cnt=0;
        long long ans=0;
        int mod= 1e9+7;
        
        while(i<n)
        {
            while(j<n && s[j]== s[i])
            {
                cnt++;
                j++;
            }
            
            cnt++;
            ans= (ans+ (cnt* (cnt-1)/2) % mod) % mod;
            cnt=0;
            i=j;
        }
        
        return ans;
        
    }
};
