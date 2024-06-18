class SegmentTree{
    public:
    vector<int> arr;
    vector<int> tree;

    SegmentTree(){}

    SegmentTree(vector<int> arr)
    {
        this->arr = arr;
        int n= arr.size();
        tree.resize(4*n, 0);
        buildTree(0, n-1, 0);
    }

    void buildTree(int l, int r, int idx);
    void updateIndex(int l, int r, int t_idx, int idx, int val);
    int query(int l, int r, int t_idx, int ql, int qr);
};

void SegmentTree:: buildTree(int l, int r, int t_idx)
{
    if(l==r)
    {
        tree[t_idx]= arr[l];
        return;
    }
    int mid = (l+r)/2;
    
    buildTree(l, mid, t_idx*2+1);
    buildTree(mid+1, r, t_idx*2+2);

    tree[t_idx]= max(tree[t_idx*2+1], tree[t_idx*2+2]); //change here for type of query, current is sum
}

void SegmentTree:: updateIndex(int l, int r, int t_idx, int idx, int val)
{
    if(l==r)
    {
        tree[t_idx]= val;
        return;
    }

    int mid = (l+r)/2;

    if (idx <= mid)
    {
        updateIndex(l, mid, t_idx*2+1, idx, val);
    }
    else
    {
        updateIndex(mid+1, r, t_idx*2+2, idx, val);
    }

    tree[t_idx]= max(tree[t_idx*2+1], tree[t_idx*2+2]); // change here for type of query, current is sum
}

int SegmentTree:: query(int l, int r, int t_idx, int ql, int qr)
{
    if (qr < l || ql > r) // out of range
    {
        return 0; //change here for type of query
    }

    if(l>= ql and r<= qr) // complete overlap
    {
        return tree[t_idx];
    }

    int mid = (l+r)/2;

    //partial overlap
    return max(query(l, mid, t_idx*2+1, ql, qr), query(mid+1, r, t_idx*2+2 , ql, qr)); // change here for type of query, current is max
};

class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        // TC: O(NLOGN) SC: O(1)
        int m= worker.size();
        int n= difficulty.size();
        vector<pair<int,int>> d_idx;
        for(int i=0; i<n; i++)
        {
            d_idx.push_back({difficulty[i], i});
        }
        
        sort(d_idx.begin(), d_idx.end());
        
        vector<int> newDifficulty;
        vector<int> newProfit;
        
        for(int i=0; i<n; i++)
        {
            newDifficulty.push_back(d_idx[i].first);
            newProfit.push_back(profit[d_idx[i].second]);
        }
        
        int ans=0;
        SegmentTree s(newProfit);
        
        for(int i=0; i<m; i++)
        {
            int r= upper_bound(newDifficulty.begin(), newDifficulty.end(), worker[i])- newDifficulty.begin();
            r--;
            
            // cout<<r<<" "<<s.query(0, n-1, 0, 0, r)<<endl;
            ans+= s.query(0, n-1, 0, 0, r);
        }
        
//         for(int i=0; i<n; i++)
//             cout<<newDifficulty[i]<<" ";
//         cout<<endl;
        
//         for(int i=0; i<n; i++)
//             cout<<newProfit[i]<<" ";
//         cout<<endl;
        
        return ans;
    }
};
