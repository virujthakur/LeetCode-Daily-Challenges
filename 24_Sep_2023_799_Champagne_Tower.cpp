class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        //TC: O(100* 100) SC: O(100* 100)
        vector<vector<double>> glasses(102, vector<double>(102));
        glasses[0][0]= poured;
        
        for (int r = 0; r <= query_row; ++r) {
            for (int c = 0; c <= r; ++c) {
                double q = (glasses[r][c] - 1.0) / 2.0;
                if (q > 0) {
                    glasses[r+1][c] += q;
                    glasses[r+1][c+1] += q;
                }
            }
        }
        
        return min(1.0, glasses[query_row][query_glass]);
    }
};
