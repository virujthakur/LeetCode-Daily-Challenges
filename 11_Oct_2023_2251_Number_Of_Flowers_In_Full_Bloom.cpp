class Solution {
public:
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& people) {
        
        int n= flowers.size();
        //sort(people.begin(), people.end());
        int q= people.size();
        sort(flowers.begin(), flowers.end());
        vector<pair<int,int>> p;
        
        for(int i=0; i<q; i++)
            p.push_back({people[i],i});
        
        sort(p.begin(),p.end());
        
        vector<int> ans(q);
        multiset<pair<int,int>> m;
        int j=0;
        for(int i=0; i<q; i++)
        { 
            while(j < n && flowers[j][0] <= p[i].first )
            {
                m.insert({flowers[j][1],flowers[j][0]}) ;
                j++ ;
            }
            while(!m.empty() && m.begin()->first < p[i].first)
            {
                m.erase(m.begin());
            }
            
            ans[p[i].second]= m.size();
            //cout<<ans[p[i].second]<<endl;
        }
        
        return ans;
    }
};
