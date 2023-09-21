class Solution {
public:
    //TC: O(LOG(min(m,n))) SC: O(1)
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        int n= nums1.size();
        int m= nums2.size();
        int sz= n+m;
        
        if(n>m)
            return findMedianSortedArrays(nums2, nums1);
        
        int mxPickupFrom1= (n+m+1)/2;
        int l=0;
        int h= n;
        
        while(l<=h)
        {
            int mid1= (l+h)/2; //pickup from 1
            // cout<<mid1<<endl;
            int mid2= mxPickupFrom1- mid1; //pickup from 2
            
            int l1= INT_MIN, l2= INT_MIN;
            int r1= INT_MAX, r2= INT_MAX;
            
            if(mid1<n) r1= nums1[mid1];
            if(mid2<m) r2= nums2[mid2];
            if(mid1-1>=0) l1= nums1[mid1-1];
            if(mid2-1>=0) l2= nums2[mid2-1];
            
            if(l1<=r2 && l2<=r1)
            {
                if(sz%2) return max(l1, l2);
                return ((double)(max(l1,l2)+ min(r1, r2)))/ 2.0;
            }
            else if(l1> r2)
                h= mid1-1;
            else
                l= mid1+1;
        }
        
        return 0.0;
        
    }
};
