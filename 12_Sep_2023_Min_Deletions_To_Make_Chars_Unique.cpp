class Solution {
public:
//     map<pair<int,vector<int>>, int> dp;
//     int recur(string& s, int i, vector<int>& freq)
//     {
//         // cout<<i<<endl;
//         if(i== s.size())
//         {
//             unordered_map<int,int> freqOfFreq;
//             int count=0;
//             for(int i=0;i<26;i++)
//             {
//                 if(freq[i]>0)
//                 {
//                     count++;
//                     freqOfFreq[freq[i]]++;
//                 }
//             }
            
//             if(count== freqOfFreq.size())
//             {
//                 return 0;
//             }
//             else 
//                 return 1e9;
//         }
        
//         if(dp.count({i,freq})) return dp[{i,freq}];
//         int ans=1e9;

//         ans= min(ans, 1+ recur(s,i+1,freq));
        
//         freq[s[i]-'a']++;
//         ans= min(ans, recur(s,i+1,freq));
//         freq[s[i]-'a']--;
//         return dp[{i,freq}]= ans;
//     }
    
    int minDeletions(string s) {
        
        vector<int> freq(26,0);
        unordered_set<int> visited;
        
        for(auto c: s) freq[c-'a']++;
        
        sort(freq.begin(), freq.end(), greater<int>());
        int ops=0;
        
        for(auto &f: freq)
        {
            if(visited.count(f))
            {
                while(f>0 && visited.count(f))
                {
                    f--;
                    ops++;
                }
            }
            
            if(f>0)
                visited.insert(f);
        }
        
        return ops;
        
    }
};