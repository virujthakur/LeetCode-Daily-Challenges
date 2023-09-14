class Solution {
public:
    
    //TC: O(E) SC: O(E) Eulerian Path, visit each edge exactly once
    vector<string> answer;
    
    void dfs(string src, unordered_map<string, priority_queue<string, vector<string>, greater<string>>>& graph)
    {
        // cout<<src<<endl;   
        auto &pq= graph[src];
        while(!pq.empty())
        {
            auto x= pq.top();
            pq.pop();
            dfs(x,graph);
        }
        answer.push_back(src);
    }
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        
        unordered_map<string, priority_queue<string, vector<string>, greater<string>>> graph;
        for(auto ticket: tickets)
            graph[ticket[0]].push(ticket[1]);
        
        dfs("JFK", graph);
        reverse(answer.begin(), answer.end());
        return answer;
        
    }
};