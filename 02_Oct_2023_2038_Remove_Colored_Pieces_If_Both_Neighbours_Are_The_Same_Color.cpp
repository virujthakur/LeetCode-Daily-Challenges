class Solution {
public:
    bool winnerOfGame(string colors) {
        int n= colors.size();
        
        int a=0;
        int b=0;
        
        int sum=0, result=0;
        for(int i=0;i<n;i++)
        {
            if(colors[i]=='A')
                sum++;
            else
            {
                if(sum>2)
                {
                    result+=sum-2;
                    sum=0;
                }
                else
                    sum=0;
            }
        }
        
        if(sum>2) result+= sum-2;
        int Alice= result;
        
        sum=0;
        result=0;

        for(int i=0;i<n;i++)

        {

            if(colors[i]=='B')

                sum++;

            else

            {

                if(sum>2)

                {

                    result+=sum-2;

                    sum=0;

                }
                else
                    sum=0;

            }

        }

        

        if(sum>2) result+= sum-2;
        
        int Bob= result;
        //cout<<Alice<<" "<<Bob<<endl;
        
        return Alice > Bob;
        
    }
};
