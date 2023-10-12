/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */
//TC: 3LOG(N), SC: O(1)
class Solution {
public:
    int binary_search1(int l, int h, int target, MountainArray &mountainArr)
    {
        int ans= INT_MAX;

        while(l<=h)
        {
            int mid= (l+h)/2;
            int ele= mountainArr.get(mid);

            if(ele== target)
            {
                ans= min(ans,mid);
                // h= mid-1;
                break;
            }
            else if(ele > target)
            {
                h= mid-1;
            }
            else
            {
                l= mid+1;
            }
        }

        return ans== INT_MAX? -1: ans;
    }
    
    int binary_search2(int l, int h, int target, MountainArray &mountainArr)
    {
        int ans= INT_MAX;

        while(l<=h)
        {
            int mid= (l+h)/2;
            int ele= mountainArr.get(mid);

            if(ele== target)
            {
                ans= min(ans,mid);
                // h= mid-1;
                break;
            }
            else if(ele < target)
            {
                h= mid-1;
            }
            else
            {
                l= mid+1;
            }
        }

        return ans== INT_MAX? -1: ans;
    }
    
    int findInMountainArray(int target, MountainArray &mountainArr) {
        
        int n = mountainArr.length();
        
        int l= 0;
        int h= n-1;
        int m_idx=-1;
        
        while(l<=h)
        {
            int mid= (l+h)/2;
            int ele= mountainArr.get(mid);
            int l_ele=-1;
            int r_ele=-1;
            
            if(mid-1 >=0)
                l_ele= mountainArr.get(mid-1);
            
            if(mid+1 < n)
                r_ele= mountainArr.get(mid+1);
            
            if(ele > r_ele && ele > l_ele)
            {
                m_idx= mid;
                break;
            }
            else if(ele > r_ele && ele < l_ele)
            {
                h= mid-1;
            }
            else
            {
                l= mid+1;
            }     
        }
        
        int ans1= binary_search1(0,m_idx,target,mountainArr);
        int ans2= binary_search2(m_idx,n-1,target,mountainArr);
        
        if(ans1==-1) return ans2;
        if(ans2==-1) return ans1;
        
        return (min(ans1,ans2));
        
    }
};
