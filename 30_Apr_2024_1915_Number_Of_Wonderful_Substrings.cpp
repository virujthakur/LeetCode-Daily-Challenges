class Solution {
public: 
    // TC: O(N* A) SC: O(A)
    long long wonderfulSubstrings(string word) {
        long long ans = 0;
        int n= word.size();
        map<string, long long> mf;
        string prevMask = "0000000000";
        mf[prevMask] = 1;
        
        for(int i=0; i<n; i++)
        {
            if(prevMask[word[i]-'a']== '1')
                prevMask[word[i] - 'a']= '0';
            else
                prevMask[word[i] - 'a']= '1';
                
            ans+= mf[prevMask];
            
            string newMask = prevMask;
            for(int j=0; j<10; j++)
            {
                newMask[j] == '0'? newMask[j]= '1' : newMask[j]= '0';
                // cout<<"( "<< newMask<<" " << mf[newMask]<<" ) ";
                ans+= mf[newMask];
                newMask[j] == '0'? newMask[j]= '1' : newMask[j]= '0';
            }
            // cout<<endl;
            
            // cout<<prevMask<<endl;
            // cout<<ans<<endl;
            mf[prevMask]+=1;
        }
        
        return ans;
    }
};
