class Solution {
public:
    //TC: O(N) SC: O(1)
    bool isDigit(char c)
    {
        if(c>='0' && c<='9')
            return true;
        return false;
    }
    
    string decodeAtIndex(string s, int k) {
        
        int n= s.size();
        long long n_chars=0;
        
        for(int i=0;i<n;i++)
        {
            if(isDigit(s[i]))
            {
                n_chars= n_chars* (s[i]-'0');
                   
            }
            else n_chars++;
        }
        // cout<<n_chars<<endl;
        
        for(int i=n-1; i>=0; i--)
        {
            k= k % n_chars;
            if(k==0 && !isDigit(s[i]))
            {
                string ans;
                ans.push_back(s[i]);
                return ans;
            }
            
            if(isDigit(s[i]))
            {
                n_chars/= s[i]-'0';
            }
            else
            {
                n_chars--;
            }
        }
        
        return "-1";
    }
};
