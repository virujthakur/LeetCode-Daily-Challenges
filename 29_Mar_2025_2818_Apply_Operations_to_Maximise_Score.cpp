const int N= 1e5+1;
bool isPrime[N];
int primeScore[N];
int mod= 1e9+7;

class Solution {
public:
    void seive()
    {
        memset(isPrime, true, sizeof(isPrime));
        memset(primeScore, 0, sizeof(primeScore));
        
        isPrime[0]= isPrime[1]= false;
        
        for(int i=2; i<N; i++)
        {
            if(isPrime[i])
            {
                primeScore[i]+=1;
                for(int j= i+i; j<N; j+=i)
                {
                    primeScore[j]+=1;
                    isPrime[j]= false;
                }
            }
        }
    }
    
    long long fastPow(long long a, long long b)
    {
        long long result=1;
        while(b>0)
        {
            if(b%2==1)
            {
                result = (result * a) % mod;
                b--;
            }
            else
            {
                a= (a* a)% mod;
                b/=2;
            }
        }
        
        return result;
    }
    
    int maximumScore(vector<int>& nums, int k) {
        seive();
        
        int n= nums.size();
        
        vector<int> scoreNums(n,0);
        
        for(int i=0;i<n;i++)
            scoreNums[i]= primeScore[nums[i]];
        
        // nextGreater Prime Score to the right of index i
        
        vector<long long> r(n,n);
        stack<int> st;
        for(int i=n-1; i>=0; i--)
        {
            if(!st.empty())
            {
                while(!st.empty() && scoreNums[st.top()] <= scoreNums[i])
                    st.pop();
                
                if(!st.empty())
                    r[i]= st.top();
            }
            st.push(i);
        }
        
        while(!st.empty()) st.pop();
        
        //nextGreater Prime Score to the left of index i;
        vector<long long> l(n,-1);
        for(int i=0; i<n; i++)
        {
            if(!st.empty())
            {
                while(!st.empty() && scoreNums[st.top()] < scoreNums[i])
                    st.pop();
            
                if(!st.empty())
                    l[i]= st.top();
            }
            st.push(i);
        }
        
        // ans calculation for every element (i-l) * (r-i)
        long long ans=1;
        priority_queue<pair<int,int>> pq;
        
        for(int i=0;i<n;i++) pq.push({nums[i],i});
        
        while(!pq.empty() && k>0)
        {
            auto x= pq.top();
            int num= x.first;
            int idx= x.second;
            long long subarrays= (idx-l[idx])* (r[idx]-idx);
            // cout<<subarrays<<" "<< num<< " " << idx-l[idx] <<" " << r[idx]-idx<< endl;
            
            if(k >= subarrays)
            {
                ans = (ans * fastPow(num, subarrays)) % mod;
                // ans*= pow(num, subarrays);
                // cout<<fastPow(num, subarrays)<<endl;
                // cout<<pow(num, subarrays)<<endl;
                k-= subarrays;
            }
            else
            {
                ans = (ans * fastPow(num, k)) % mod;
                // ans*= pow(num, k);
                // cout<<fastPow(num,k)<<endl;
                // cout<<pow(num,k)<<endl;
                k=0;
            }
            pq.pop();
        }
        
//         for(int i=0;i<n;i++)
//             cout<<scoreNums[i]<<" ";
//         cout<<endl;
        
//         for(int i=0;i<n;i++)
//             cout<<l[i]<<" ";
//         cout<<endl;

//         for(int i=0;i<n;i++)
//             cout<<r[i]<<" ";
//         cout<<endl;
        
        return ans% mod;

    }
};
