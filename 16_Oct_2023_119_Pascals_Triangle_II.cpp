class Solution {
public:
    
    //TC: O(rowIndex * rowIndex) SC: O(rowIndex)
    vector<int> getRow(int rowIndex) {
        
        if(rowIndex == 0)
            return {1};
        
        vector<int> ans;
        
        vector<int> triangle;
        triangle= {1,1};
        
        for(int i=2; i<=rowIndex ; i++)
        {
            vector<int> row;
            row.push_back(1);
            
            for(int j=1; j<i; j++)
            {
                // cout<< triangle[i-1][j-1]+ triangle[i-1][j]<< endl;
                row.push_back(triangle[j-1]+ triangle[j]);
            }
            
            row.push_back(1);
            triangle= row;
        }
        
        return triangle;
    }
};
