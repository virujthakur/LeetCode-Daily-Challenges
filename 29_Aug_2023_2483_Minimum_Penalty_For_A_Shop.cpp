class Solution {
public:
    int bestClosingTime(string customers) {
        
        //TC: O(N) SC: O(N)
        // Using prefix sum arrays to calculate the number of Y's and N's before 
        // and after a particular hour 'i'
        int n= customers.size();
        vector<int> prefixY(n,0);
        vector<int> prefixN(n,0);
        
        int totalY=0, totalN=0;
        
        for(int i=0; i<n; i++)
        {
            if(customers[i]=='Y')
                totalY++;
            if(customers[i]=='N')
                totalN++;
            prefixY[i]= totalY;
            prefixN[i]= totalN;
        }
        
        int penalty= INT_MAX;
        int ans=-1;
        for(int i=0; i<n; i++)
        {
            // cout<<prefixN[i]<<" "<<totalY<<" "<<prefixY[i]<<endl;
            int p= (i-1>=0 ? prefixN[i-1]: 0)+ totalY- (i-1>=0? prefixY[i-1]: 0);
            // cout<<p<<endl;
            if(penalty > p)
            {
                penalty= p;
                ans=i;
            }
        }
        
        int p= totalN;
        if(penalty > p)
        {
            penalty=p;
            ans=n;
        }
        
        return ans;
    }
};