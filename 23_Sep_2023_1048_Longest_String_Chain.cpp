//TC: O(N^2 * 16^2) SC: O(N^2)
bool compare(string& s1, string& s2)
{
    if(s1.size()!= s2.size())
        return s1.size()< s2.size();
    else
        return s1<s2;
}

class Solution {
public:
    
    bool isValid(string& s1, string& s2)
    {
        if(s2.size()-s1.size()>1 || s2.size()==s1.size())
            return false;
        
        int n= s2.size();
        for(int i=0;i<n;i++)
        {
            string temp= s2;
            temp.erase(i,1);
            if(temp== s1)
                return true;
        }
        
        return false;
            
    }
    
    int longestStrChain(vector<string>& words) {
        int n= words.size();
        sort(words.begin(), words.end(), compare);
        
        // for(auto word: words)
        //     cout<<word<<" ";
        // cout<<endl;
        
        vector<int> dp(n,1);
        
        for(int i=0;i<n;i++)
        {
            for(int j=0; j<i; j++)
            {
                if(isValid(words[j], words[i]))
                    dp[i]= max(dp[i], dp[j]+1);
            }
        }
        
        return *max_element(dp.begin(), dp.end());
    }
};
