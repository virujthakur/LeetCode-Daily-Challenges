// provide l, r (range index of the array to build tree on) and t_idx=0 (tree iterator) to every method)
class SegmentTree{
    public:
    vector<int> arr;
    vector<int> tree;

    SegmentTree(){}

    SegmentTree(vector<int> arr)
    {
        this->arr = arr;
        int n= arr.size();
        tree.resize(4*n, -1);
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
        return -1; //change here for type of query
    }

    if(l>= ql and r<= qr) // complete overlap
    {
        return tree[t_idx];
    }

    int mid = (l+r)/2;

    //partial overlap
    return max(query(l, mid, t_idx*2+1, ql, qr), query(mid+1, r, t_idx*2+2 , ql, qr)); // change here for type of query, current is sum
}

class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        int n= nums.size();
        vector<int> place(5e4+1, -1);
        SegmentTree s(place);
        int ans = 0;
        
        for(int j= n-1; j>=0; j--)
        {
            if (s.query(0,5e4,0, nums[j], nums[j]) == -1)
                s.updateIndex(0, 5e4, 0, nums[j], j);
            // cout<<s.query(0, 5e4, 0, nums[j], 5e4)<<endl;
            ans = max(ans, s.query(0, 5e4, 0, nums[j], 5e4)- j);
        }
        
        return ans;
    }
};
