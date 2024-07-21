class Solution {
public:
    vector<vector<int>> buildMatrix(int k, vector<vector<int>>& rowConditions, vector<vector<int>>& colConditions) {
        
        vector<int> x = TopoSort(rowConditions, k) ;
        vector<int> y = TopoSort(colConditions, k) ;
        
        if(x.empty() || y.empty())
            return {} ;
        
        vector<vector<int>> ans(k, vector<int>(k,0)) ;
        
        vector<int> rowIdx(k+1) ;
        vector<int> colIdx(k+1) ;
        
        for(int i = 0 ; i < k ; i++)
        {
            rowIdx[x[i]] = i ;
            colIdx[y[i]] = i ;
        }
        
        for(int i = 1 ; i <= k ; i++)
        {
            ans[rowIdx[i]][colIdx[i]] = i ;
        }
        
        return ans ;
    }
    
    vector<int> TopoSort(vector<vector<int>> &edges, int sz)
    {
        vector<int> inDeg(sz+1,0) ;
        vector<vector<int>> Graph(sz+1);
        
        for(auto e : edges)
        {
            Graph[e[0]].push_back(e[1]) ;
            inDeg[e[1]]++ ;
        }
        
        queue<int> q ;
        
        for(int i = 1 ; i <= sz ; i++)
        {
            if(inDeg[i] == 0)
               q.push(i) ;
        }
        
        int count = 0 ;
        vector<int> ans ;
        
        while(!q.empty())
        {
            int v = q.front() ;
            q.pop() ;
            count++ ;
            ans.push_back(v) ;
            
            for(auto c : Graph[v])
            {
                inDeg[c]-- ;
                if(inDeg[c] == 0)
                {
                    q.push(c) ;
                }
            }
        }
        
        vector<int> temp ;
        
        return count == sz ? ans : temp ;
    }
};
