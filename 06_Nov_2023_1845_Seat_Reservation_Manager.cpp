//TC: O(NLOGN) SC; O(N)
class SeatManager {
public:
    set<int> unr;
    SeatManager(int n) {
        
        for(int i=1; i<=n ;i++)
            unr.insert(i);
    }
    
    int reserve() {
        int s= *unr.begin();
        unr.erase(unr.begin());
        return s;
    }
    
    void unreserve(int seatNumber) {
        unr.insert(seatNumber);
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */
