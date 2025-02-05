class Solution {
public:
    // TC: O(N) SC: O(1)
    bool areAlmostEqual(string s1, string s2) {
        int diff = 0;
        unordered_map<char,int> f;
        int n= s1.size();
        for(int i=0; i<n; i++){
            diff += s1[i]!= s2[i];
            f[s1[i]] += 1;
            f[s2[i]] -=1;
        }

        if (diff >2)
        return false;

        for(auto x: f){
            if (x.second != 0){
                return false;
            }
        }

        return true;
    }
};
