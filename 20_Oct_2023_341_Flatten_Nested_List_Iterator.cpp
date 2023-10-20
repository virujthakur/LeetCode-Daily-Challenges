/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
public:
    int i=0;
    vector<int> res;
    
    NestedIterator(vector<NestedInteger> &nestedList) {
     
        flatten(nestedList);
    }
    
    void flatten(vector<NestedInteger> nestedList)
    {
        int n= nestedList.size();
        
        for(int i=0; i<n;i++)
        {
            if(nestedList[i].isInteger())
                res.push_back(nestedList[i].getInteger());
            else
                flatten(nestedList[i].getList());
        }
    }
    
    int next() {
        
        int ans= res[i];
        i++;
        return ans;
    }
    
    bool hasNext() {
        // cout<<res.size()<<endl;
        // for(int j=0; j<res.size(); j++)
        //     cout<<res[j]<<" ";
        // cout<<endl;
        // cout<<(i==res.size())<<endl;
        return i!= res.size();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
