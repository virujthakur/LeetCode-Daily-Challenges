class Solution {
public:
    
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        vector<pair<int, int>> pairs;

        for(int i = 0; i < capital.size(); i++)
            pairs.push_back({capital[i], profits[i]});

        sort(pairs.begin(), pairs.end());

        int i = 0;
        priority_queue<int> pq;

        while(k--)
        {
            while(i < pairs.size() && w >= pairs[i].first)
            {
                pq.push(pairs[i].second);
                i++;
            }

            if(pq.empty())
                break;
            
            w += pq.top();
            pq.pop();
        }

        return w;
    }
};
