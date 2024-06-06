class Solution {
public:
    //TC: O(N) SC: O(N)
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        int n= hand.size();
        map<int,int> f;
        for(auto num: hand)
            f[num]+=1;
        
        while(!f.empty())
        {
            int mn= f.begin()->first;
            for(int i=0; i<groupSize; i++)
            {
                if(f[mn]== 0)
                    return false;
                
                f[mn]-=1;
                
                if (f[mn]== 0)
                    f.erase(mn);
                mn+=1;
            }
            //make group
        }
        
        return true;
    }
};
