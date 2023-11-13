//TC: O(NLOGN) SC: O(N)
class Solution {
public:
    string sortVowels(string s) {
        
        set<char> vowels= {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        multiset<char> m;
        for(auto c: s)
        {
            if(vowels.count(c))
                m.insert(c);
        }
        
        for(auto& c: s)
        {
            if(vowels.count(c))
            {
                c= *m.begin();
                m.erase(m.begin());
            }
        }
        
        return s;
    }
};
