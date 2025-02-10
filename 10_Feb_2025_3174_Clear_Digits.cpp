class Solution {
public:
    // TC: O(N) SC: O(N)
    string clearDigits(string s) {
        stack<int> st;
        for(auto c: s)
        {
            if(c >='0' && c<='9')
            {
                if (!st.empty()){
                    st.pop();
                }
            }
            else{
                st.push(c);
            }
        }

        string ans;
        while(!st.empty()) 
        {
            ans.push_back(st.top());
            st.pop();
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};
