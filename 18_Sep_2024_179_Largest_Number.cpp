//TC: O(NLOGN) SC: O(N)
bool compare(string& a, string &b)
{
    int m= a.size();
    int n= b.size();
    string one = a+b;
    string two = b+a;
    
    return stoull(one) > stoull(two);
}

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        int n= nums.size();
        vector<string> newnums;
        for(auto num: nums)
            newnums.push_back(to_string(num));
        
        sort(newnums.begin(), newnums.end(), compare);
        
        string ans;
        for(auto num: newnums)
            ans+= num;
        
        reverse(ans.begin(), ans.end());
        while(ans.back()== '0' and ans.size() > 1)
            ans.pop_back();
        reverse(ans.begin(), ans.end());
        
        return ans;
    }
};
