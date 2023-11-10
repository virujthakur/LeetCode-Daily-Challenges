// TC: O(N) SC: O(N)
class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        
        // elements with indegree 1 will be the terminals in the array
        // the adjacent elements to the terminals will the
        // penultimate terminals
        
        // 4-> 3 -> 2 -> 1
        int n= adjacentPairs.size()+1;
        unordered_map<int, int> indegree;
        unordered_map<int, vector<int>> graph;
        
        for(auto p: adjacentPairs)
        {
            indegree[p[0]]++;
            indegree[p[1]]++;
            graph[p[0]].push_back(p[1]);
            graph[p[1]].push_back(p[0]);
        }
        
        queue<int> q;
        for(auto x: indegree)
            if(x.second==1)
                q.push(x.first);
        
        vector<int> ans(n);
        bool flag= true;
        int i=0; int j= n-1;
        
        while(!q.empty())
        {
            auto x= q.front();
            q.pop();
            if(flag)
            {
                ans[i]= x;
                i++;
            }
            else
            {
                ans[j]=x;
                j--;
            }
            flag= !flag;
                
            for(auto y: graph[x])
            {
                indegree[y]--;
                if(indegree[y]==1)
                    q.push(y);
            }
        }
        
        return ans;
        
        
    }
};
