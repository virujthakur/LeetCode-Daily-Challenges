class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        
        vector<int> maxReach(n+1,0);
        
        for(int i=0;i < ranges.size(); i++)
        {   
            int l= i- ranges[i];
            int r= i+ ranges[i];
            l = max(l,0);
            r = min(r,n);
            
            maxReach[l]= max(maxReach[l], r);    
        }
        
        int curEnd=0;
        int nextEnd=0;
        int ans=0;
        
        for(int i=0;i<=n; i++)
        {
            if(i> nextEnd)
                return -1;
            
            if(i> curEnd)
            {
                ans++;
                curEnd= nextEnd;
            }
            
            nextEnd= max(nextEnd, maxReach[i]);
        }
        
        return ans;
    }
};