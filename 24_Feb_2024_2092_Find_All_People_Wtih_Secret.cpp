class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        sort(meetings.begin(), meetings.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[2] < b[2];
        });
        
        vector<int> have;
        vector<int> parent(n);
        vector<int> rank(n);

        for (int i = 0; i < n; ++i) {
            parent[i] = i;
            rank[i] = 0;
        }

        function<int(int)> find = [&](int x) {
            if (x == parent[x]) {
                return x;
            }
            parent[x] = find(parent[x]);
            return parent[x];
        };

        function<void(int, int)> unionf = [&](int x, int y) {
            int px = find(x);
            int py = find(y);
            if (px == py) {
                return;
            }

            if (rank[px] < rank[py]) {
                parent[px] = py;
            } else if (rank[px] > rank[py]) {
                parent[py] = px;
            } else {
                parent[py] = px;
                rank[py]++;
            }
        };

        unionf(0, firstPerson);

        for (int i = 0; i < meetings.size(); ++i) {
            int t = meetings[i][2];
            int j = i;
            while (j < meetings.size() && meetings[j][2] == t) {
                unionf(meetings[j][0], meetings[j][1]);
                j++;
            }

            j = i;
            while (j < meetings.size() && meetings[j][2] == t) {
                if (find(meetings[j][0]) != find(0)) {
                    parent[meetings[j][0]] = meetings[j][0];
                    parent[meetings[j][1]] = meetings[j][1];
                    rank[meetings[j][0]] = 0;
                    rank[meetings[j][1]] = 0;
                }
                j++;
            }

            i = j - 1;
        }

        for (int i = 0; i < n; ++i) {
            if (find(i) == find(0)) {
                have.push_back(i);
            }
        }

        return have;
    }
};
