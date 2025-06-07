class Solution {
public:
    //TC: O(NLOGN) SC: O(N)
    string clearStars(string s) {
        int n = s.size();
        auto customComparator = [](const pair<char,int>& a, const pair<char,int>& b) { 
            if (a.first != b.first){
                return a.first < b.first;
            }   
            else{
                return a.second > b.second;
            }
            };
        
        multiset<pair<char, int>, decltype(customComparator)> m;

        for (int i=0; i<n; i++){
            if (s[i] == '*'){
                if (m.size() > 0){
                    m.erase(m.begin());
                }
            }
            else{
                m.insert({s[i], i});
            }
        }

        string temp(n, '.');
        for (auto x: m)
            temp[x.second]= x.first;

        string ans;
        for (int i=0; i<n; i++)
            if (temp[i] != '.')
                ans.push_back(temp[i]);

        return ans;

    }
};
