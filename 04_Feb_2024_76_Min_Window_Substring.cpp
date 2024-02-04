class Solution {
public:
    string minWindow(string s, string t) {
        
        // TC: O(M+N) SC: O(1)
        int m= s.size();
        vector<int> mapt(52);
        int ast= -1;
        int aen= -1;
        int dmc= t.size();
        
        for(int i=0;i<t.size();i++)
        {
            if(t[i]>='a' && t[i]<='z')
                mapt[t[i]-'a']++;
            else
                mapt[t[i]-'A' + 26] ++;
        }
        
        int i=0;
        int j=0;
        
        while(i<m)
        {
            while(i<m && dmc > 0)
            {
                if(s[i]>='a' && s[i]<='z')
                {
                    if(mapt[s[i]-'a'] > 0)
                        dmc--;
                    mapt[s[i]-'a']--;   
                }
                else
                {
                    if(mapt[s[i]-'A'+ 26] > 0)
                        dmc--;
                    mapt[s[i]-'A' + 26] --;
                }
                i++;
            }
            
            // cout<< i<<" "<<j<<" "<<dmc<<endl;
            while(j<i && dmc== 0)
            {
                if(ast== -1 || (i-j < aen- ast+ 1))
                {
                    ast= j;
                    aen= i-1;
                }
                
                if(s[j]>='a' && s[j]<='z')
                {
                    mapt[s[j]-'a']++;
                    if(mapt[s[j]-'a'] > 0)
                        dmc++;
                }
                else
                {
                    mapt[s[j]-'A' + 26]++;
                    if(mapt[s[j]-'A'+ 26] > 0)
                        dmc++;   
                }
                
                j++;
            }
            
        }
        
        return (ast != -1? s.substr(ast, aen-ast+1) : "");
        
    }
};
