class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        sort(left.begin(), left.end());
        sort(right.begin(), right.end());
        
        return max(left.size()> 0 ? left.back(): 0, right.size() >0 ?  n- right.front(): 0);
    }
};
