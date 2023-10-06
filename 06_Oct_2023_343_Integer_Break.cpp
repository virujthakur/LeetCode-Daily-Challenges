class Solution {
public:
    int integerBreak(int n) {
        
        int sum= n;
        long long prod= n/2 * (n- (n/2));
        
        for(int i=3; (n/i)>0 ; i++)
        {
            long long newProd=1;
            vector<long long> v;
            long long tempSum= n;
            
            for(int j=0; j<i; j++)
            {
                v.push_back(n/i);
            }
            
            long long rem= n%i;
            for(int j=0; j<v.size(); j++)
            {
                if(rem>0)
                {
                    v[j]++;
                    rem--;
                }
            }
            
            for(int j=0; j<v.size(); j++)
                newProd*= v[j];
            
            prod= max(prod, newProd);
            //cout<<newProd<<endl;
            

        }
        return prod;
    }
};
