class Solution {
public:
    //TC: O(N) SC:O(1)
    bool isSubsequence(string s, string t) {
        
        // if(s==t)
        //     return true;
        
        int n= s.size();
        
        int j=0;
        int i=0;
        for(i=0;i<n;i++)
        {
            // cout<<i<<" "<<j<<endl;
            // cout<<s[i]<<" "<<t[j]<<endl;
            char c= s[i];
            while(j<t.size() && t[j]!=c) j++;
            j++;
            
            if(j>t.size())
                break;
        }
        
        if(i==n) return true;
        else
            return false;
        
    }
};
