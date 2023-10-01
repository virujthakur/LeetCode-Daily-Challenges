class Solution {
public:
    string reverseWords(string s) {
        
        string word;
        string ans;
        for(auto c: s)
        {
            if(c==' ')
            {
                reverse(word.begin(), word.end());
                ans+= word;
                ans+= ' ';
                word.clear();
            }
            else
                word.push_back(c);
        }
        
        reverse(word.begin(), word.end());
        ans+=word;
        // ans.pop_back();
        return ans;
    }
};
