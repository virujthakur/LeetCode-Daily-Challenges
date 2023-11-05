//TC: O(N) SC:O(1)
class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        
        int n= arr.size();
        int mx= *max_element(arr.begin(), arr.end());
        queue<int> q;
        
        for(auto num: arr) q.push(num);
        
        int cur= q.front();
        q.pop();
        
        int streak =0;
        
        while(!q.empty())
        {
            int op= q.front();
            q.pop();
            if(cur > op)
            {
                q.push(op);
                streak++;
            }
            else
            {
                q.push(cur);
                cur= op;
                streak=1;
            }
            
            if(streak ==k || mx== cur)
                return cur;
        }
        
        return -1;
        
    }
};
