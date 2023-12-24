class Solution {
public:
    int minOperations(string s) {
        int n= s.size();
        string s1, s2;
        for(int i=0; i<n; i++)
        {
            if(i%2)
            {
                s1.push_back('1');
                s2.push_back('0');
            }
            else
            {
                s1.push_back('0');
                s2.push_back('1');
            }
        }
        
        function<int(string&, string&)> getValue= [&](string& s1, string& s2)-> int
        {
            int ans=0;
            for(int i=0; i<s.size(); i++)
            {
                if(s1[i]!= s2[i])
                    ans++;
            }
            
            return ans;
        };
        
        return min(getValue(s,s1), getValue(s,s2));       
        
    }
};
