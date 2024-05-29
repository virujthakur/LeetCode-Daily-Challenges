class Solution {
public:
    //TC: O(N^3) SC: O(1)
    bool isOne(string s)
    {
        for(int i=0; i<s.size()-1; i++)
        {
            if(s[i] == '1')
                return false;
        }
        
        return s.back() == '1';
    }
    
    string addOne(string s)
    {
        int c= 1;
        for(int i= s.size()-1; i>=0; i--)
        {
            if (s[i]=='1' and c== 1)
                s[i]= '0';
            else if (s[i]== '1' and c== '0')
            {
                s[i]='1';
                c= 0;
            }
            else if(c==1 and s[i]== '0')
            {
                s[i]= '1';
                c= 0;
            }
        }
               
        if (c== 1)
            s.insert(s.begin(), '1');
        return s;
    }
    int numSteps(string s) {
        int n= s.size();
        int ans = 0;
        
        // cout<<s<<endl;
        // cout<<isOne(s)<<endl;
        
        while(!isOne(s))
        {
            // cout<<s<<endl;
            if (s.back()== '1')
            {
                s= addOne(s);
            }
            else
            {
                for(int i= s.size()-1; i>0; i--)
                {
                    s[i]= s[i-1];
                }
                
                s[0]= '0';
            }
            
            ans+=1;
        }
        
        return ans;
        
    }
};
