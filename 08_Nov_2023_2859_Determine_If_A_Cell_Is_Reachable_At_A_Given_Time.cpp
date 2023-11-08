class Solution {
public:
    bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        
        if(sx==fx && fy==sy && t==1)
            return false;
        else if(sx==fx && fy==sy)
            return true;
        
        int d1 = abs(sy-fy) ;
        int d2 = abs(sx-fx) ;
        
        int common = min(d1,d2) ;
        
        int rem = max(d1,d2) - common ;
        
        return t >= common + rem ;
    }
};
