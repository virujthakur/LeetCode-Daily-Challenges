class Solution {
public:
    //TC: O(N) SC: O(26)
    char findTheDifference(string s, string t) {
        
        int n= t.size();
        unordered_map<char,int> f;
        for(auto c:t)
            f[c]++;
        for(auto c:s)
            f[c]--;
        for(auto x:f)
            if(x.second)
                return x.first;
        
        return '#';
        
    }
};
