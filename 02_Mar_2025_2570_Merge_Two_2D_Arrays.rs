impl Solution {
    //TC :O (N) SC: O(1)
    pub fn merge_arrays(nums1: Vec<Vec<i32>>, nums2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut i =0;
        let mut j =0;
        let n = nums1.len();
        let m = nums2.len();
        let mut ans = Vec::new();

        while i < n && j< m{
            if nums1[i][0] == nums2[j][0]{
                ans.push(vec![nums1[i][0], nums1[i][1] + nums2[j][1]]);
                i+=1;
                j+=1;
            }
            else if nums1[i][0] > nums2[j][0]{
                ans.push(vec![nums2[j][0], nums2[j][1]]);
                j+=1;
            }
            else{
                ans.push(vec![nums1[i][0], nums1[i][1]]);
                i+=1;
            }
        }

        while i<n{
            ans.push(vec![nums1[i][0], nums1[i][1]]);
            i+=1;
        }

        while j<m{
            ans.push(vec![nums2[j][0], nums2[j][1]]);
            j+=1;
        }

        return ans;
    }
}
