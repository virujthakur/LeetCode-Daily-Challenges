class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int n= s.size();
        unordered_set<string> ans;
        
        unordered_map<char,int> f;
        for(auto c: s)
            f[c]++;
        unordered_map<char,int> pf;
        for(auto c: s)
        {
            for(char i='a' ; i<='z'; i++)
            {
                int sf= f[i]- pf[i]- (i==c? 1: 0);
                if(pf[i]>=1 && sf>=1)
                {
                    string temp;
                    temp.push_back(i);
                    temp.push_back(c);
                    temp.push_back(i);
                    
                    ans.insert(temp);
                }
            }
            
            pf[c]++;
        }
            
        return ans.size();
    }
};
