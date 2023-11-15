//TC: O(NLOGN) SC: O(1)
class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        int n= arr.size();
        
        sort(arr.begin(), arr.end());
        
        int cur=1;
        arr[0]=1;
        for(int i=1; i<n; i++)
        {
            if(arr[i] > cur)
            {
                cur++;
                arr[i]= cur;
            }
            else
            {
                arr[i]= cur;
            }
        }
        
        return arr[n-1];
        
    }
};
