class Graph {
public:
    
    vector<vector<pair<int,int>>> graph;
    int N;
    
    // vector<vector<int>> srctodest;
    
    Graph(int n, vector<vector<int>>& edges) {
        graph.resize(n);
        N=n;
        
        for(auto edge: edges)
        {
            int x= edge[0];
            int y= edge[1];
            int cost= edge[2];
            
            graph[x].push_back({cost,y});
        }
    }
    
    void addEdge(vector<int> edge) {
        
        int x= edge[0];
        int y= edge[1];
        int cost= edge[2];
        
        graph[x].push_back({cost,y});
    }
    
    int shortestPath(int node1, int node2) {
        
//         if(srctodest.empty()) srctodest.resize(N);
        
//         if(!srctodest[node1].empty()) return srctodest[node1][node2];
        
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        
        pq.push({0, node1});
        
        vector<int> distTo(N,INT_MAX);
        distTo[node1]=0;
        
        while(!pq.empty())
        {
            auto x= pq.top();
            int curNode= x.second;
            int curCost= x.first;
            pq.pop();
            
            for(auto n: graph[curNode])
            {
                if(distTo[n.second]== INT_MAX || distTo[n.second] > distTo[curNode]+ n.first)
                {
                    distTo[n.second]= distTo[curNode]+ n.first;
                    pq.push({distTo[n.second], n.second});
                }
            }
        }
        
        // srctodest[node1]= distTo
        return distTo[node2]== INT_MAX? -1: distTo[node2];
    }
};

/**
 * Your Graph object will be instantiated and called as such:
 * Graph* obj = new Graph(n, edges);
 * obj->addEdge(edge);
 * int param_2 = obj->shortestPath(node1,node2);
 */
