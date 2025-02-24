class Solution {
public:
    //TC: O(N) SC: O(N)
    void make_parent(vector<vector<int>>& tree, int src, vector<int>& parent, vector<bool>& visited)
    {
        visited[src]= true;
        for(auto nbr: tree[src])
        {
            if(!visited[nbr])
            {
                parent[nbr]= src;
                make_parent(tree, nbr, parent, visited);
            }
        }
    }
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        int n= amount.size();
        vector<vector<int>> tree(n);
        for(auto edge: edges)
        {
            tree[edge[0]].push_back(edge[1]);
            tree[edge[1]].push_back(edge[0]);
        }
        
        vector<int> parent(n,-1);
        vector<bool> visited(n, false);
        make_parent(tree, 0, parent, visited);
        vector<int> bobPath;
        vector<int> bobTime(n, -1);
        int t=0;

        while (bob !=-1)
        {
            bobTime[bob]= t++;
            bobPath.push_back(bob);
            bob= parent[bob];
        }

        // for(int i=0; i<n; i++)
        // {
        //     cout<<i<<" "<<bobTime[i]<<" "<<endl;
        // }
        // cout<<endl;

        int ans = INT_MIN;
        queue<vector<int>> q;
        visited.assign(n, false);
        q.push({0,0,0});

        while(!q.empty())
        {
            int curNode = q.front()[0];
            int curAliceTime= q.front()[1];
            int curIncome = q.front()[2];
            visited[curNode]= true;
            q.pop();

            int newIncome = curIncome;
            if (bobTime[curNode]== -1){
                newIncome += amount[curNode];
            }
            else{
                if(bobTime[curNode] > curAliceTime )
                {
                    newIncome += amount[curNode];
                }
                else if (bobTime[curNode] == curAliceTime){
                    newIncome += amount[curNode] / 2;
                }
            }

            // cout<<curNode<<" "<<newIncome<<endl;
            if (tree[curNode].size() == 1 && curNode !=0)
            {
                ans= max(ans, newIncome);
            }

            for(auto nbr: tree[curNode])
            {
                if(!visited[nbr])
                {
                    q.push({nbr, curAliceTime+1, newIncome});
                }
            }

        }

        return ans;
    }
};
