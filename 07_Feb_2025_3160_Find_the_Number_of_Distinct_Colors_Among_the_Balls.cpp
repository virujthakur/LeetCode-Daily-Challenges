class Solution {
public:
    //TC: O(N) SC: O(N)
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        unordered_map<int, set<int>> colorsToBalls;
        unordered_map<int, int> ballColor;

        int ans = 0;
        vector<int> answer;
        for(auto q: queries){
            int oldColor = ballColor[q[0]];
            int newColor = q[1];
            if (oldColor !=0 and oldColor != newColor){
                colorsToBalls[oldColor].erase(q[0]);
                if(colorsToBalls[oldColor].size() == 0){
                    colorsToBalls.erase(oldColor);
                }
            }

            ballColor[q[0]]= q[1];
            colorsToBalls[q[1]].insert(q[0]);
            answer.push_back(colorsToBalls.size());
        }

        return answer;
    }
};
