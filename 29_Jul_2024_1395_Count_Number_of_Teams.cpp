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

    tree[t_idx]= + tree[t_idx*2+1] + tree[t_idx*2+2]; //change here for type of query, current is sum
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

    tree[t_idx]= + tree[t_idx*2+1] + tree[t_idx*2+2]; // change here for type of query, current is sum
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
    return query(l, mid, t_idx*2+1, ql, qr)+ query(mid+1, r, t_idx*2+2 , ql, qr); // change here for type of query, current is sum
}

class Solution {
    //TC: O(N^2 LOGN) SC: O(4N)
public:
    int numTeams(vector<int>& rating) {
        int n= rating.size();
        vector<int> activation(1e5+1, 0);
        long long ans = 0;
        
        SegmentTree s(activation);        
        for(int j=n-1; j>=0; j--)
        {
            for(int i=0; i<j; i++)
            {
                if (rating[i] < rating[j])
                {
                    ans += s.query(0, 1e5, 0, rating[j]+ 1, 1e5);
                    // cout<< i<<" " <<j<<" "<< s.query(0, 1e5, 0, rating[j]+1, 1e5)<<endl;
                }
                else
                {
                    ans += s.query(0, 1e5, 0, 0, rating[j]-1);
                    // cout<< i<<" " <<j<<" "<<  s.query(0, 1e5, 0, rating[j]-1, 1e5)<<endl;
                }
            }
            
            s.updateIndex(0, 1e5, 0, rating[j], 1);
        }
        
        return ans;
    }
};
