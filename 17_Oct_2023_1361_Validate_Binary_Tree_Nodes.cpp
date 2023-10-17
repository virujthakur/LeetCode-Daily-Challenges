class Solution {
public:
    //TC: O(N) SC: O(N)
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        
        vector<vector<int>> graph(n);
        vector<int> indegree(n);
        
        for(int i=0; i<n ;i++)
        {
            if(leftChild[i]!=-1)
            {
                graph[i].push_back(leftChild[i]);
                indegree[leftChild[i]]++;
            }
            
            if(rightChild[i]!=-1)
            {
                graph[i].push_back(rightChild[i]);
                indegree[rightChild[i]]++;
            }
        }
        
        queue<int> q;
        
        for(int i=0; i<n; i++)
        {
            if(indegree[i]==0)
            {
                q.push(i);
            }
            else if(indegree[i] >=2)
                return false;        
        }
        
        if(q.size() >=2) return false;
        
        vector<int> topoSort;
        
        while(!q.empty())
        {
            auto node= q.front();
            topoSort.push_back(node);
            // int countChild= 0;
            q.pop();
            
            for(auto child: graph[node])
            {
                indegree[child]--;
                if(indegree[child]==0)
                    q.push(child);
            }
        }
        
        return topoSort.size()== n;
        
    }
};
