class Solution {
public:
    //TC: O(NLOGN) SC: O(N)
    bool isValid(vector<int>& tasks, vector<int>& workers, int pills, int strength, int mid){
        multiset<int> ws;
        int m = workers.size();

        int p = pills;
        for (int i = m - mid; i < m; ++i) {
            ws.insert(workers[i]);
        }

        for (int i = mid - 1; i >= 0; --i) {
            if (auto it = prev(ws.end()); *it >= tasks[i]) {
                ws.erase(it);
            } else {
                if (!p) {
                    return false;
                }
                auto rep = ws.lower_bound(tasks[i] - strength);
                if (rep == ws.end()) {
                    return false;
                }
                --p;
                ws.erase(rep);
            }
        }
        return true;
    }

    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        int l =0, h= min(tasks.size(), workers.size());
        sort(workers.begin(), workers.end());
        sort(tasks.begin(), tasks.end());
        int ans =0;
        while (l<=h){
            int mid = l + (h-l)/2;
            if (isValid(tasks, workers, pills, strength, mid)){
                l = mid+1;
                ans = max(ans, mid);
            }
            else{
                h= mid-1;
            }
        }

        return ans;
    }
};
