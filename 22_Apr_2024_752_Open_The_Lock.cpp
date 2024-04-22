class Solution {
public:
    // V= 10^4 E per V = 8
    // TC: O(ELOG(V)) SC: O(V)
    int openLock(vector<string>& deadends, string target) {
        priority_queue<pair<int,string>, vector<pair<int,string>>, greater<pair<int,string>>> pq;
        
        map<string, int> distTo;
        map<string, bool> visited;
        set<string> dead(deadends.begin(), deadends.end());
        
        if(!dead.count("0000"))
        {
            pq.push({0, "0000"});
            distTo["0000"]= 0;
        }
        
        while(!pq.empty())
        {
            auto cur= pq.top();
            pq.pop();
            
            string node= cur.second;
            // cout<<node<<endl;
            
            if(node == target)
                return cur.first;
            
            if(visited[node])
                continue;
            
            visited[node]= true;
            
            for(int i=0; i<4; i++)
            {
                string nbr1 = node;
                if(nbr1[i] < '9')
                    nbr1[i]+=1;
                else
                    nbr1[i]= '0';
                
                string nbr2 = node;
                
                if(nbr2[i] > '0')
                    nbr2[i]-=1;
                else
                    nbr2[i]= '9';
                // cout<<nbr1<<" "<<nbr2<<endl;
                
                if(!dead.count(nbr1) && !visited.count(nbr1) && (!distTo.count(nbr1) || distTo[nbr1] > distTo[node]+ 1))
                {
                    distTo[nbr1]= distTo[node]+1;
                    pq.push({distTo[nbr1], nbr1});
                }
                
                if(!dead.count(nbr2) && !visited.count(nbr2) && (!distTo.count(nbr2) || distTo[nbr2] > distTo[node]+ 1))
                {
                    distTo[nbr2]= distTo[node]+1;
                    pq.push({distTo[nbr2], nbr2});
                }
            }
        }
        
        return -1;
    }
};
