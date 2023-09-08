//TC : O(N^2) SC : O(1) extra space
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        
        vector<vector<int>> answer;
        answer.push_back({1});
        int n= numRows;
        
        for(int i=1; i<n ;i++)
        {
            vector<int> row;
            row.push_back(1);
            // cout<<answer[i-1].size()<<endl;
            for(int j=0; j< answer[i-1].size()-1; j++)
            {
                row.push_back(answer[i-1][j]+ answer[i-1][j+1]);
            }
            
            row.push_back(1);
            answer.push_back(row);
            // for(auto r: row)
            //     cout<<r<<" ";
            // cout<<endl;
        }
        
        return answer;
    }
};