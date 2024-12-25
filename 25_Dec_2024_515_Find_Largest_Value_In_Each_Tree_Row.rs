// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
impl Solution {
    //TC: O(N) SC: O(N)
    pub fn largest_values(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut q = VecDeque::new();
        if let Some(node) = root {
            q.push_back(node);
        }

        let mut ans = Vec::new();

        while !q.is_empty() {
            let sz = q.len();
            let mut cur_nodes = Vec::new();

            for _ in 0..sz {
                if let Some(node) = q.pop_front() {
                    let node_ref = node.borrow();
                    cur_nodes.push(node.clone());
                    if let Some(left) = &node_ref.left {
                        q.push_back(left.clone());
                    }
                    if let Some(right) = &node_ref.right {
                        q.push_back(right.clone());
                    }
                }
            }
            
            let mut mx = std::i32::MIN;
            for node in cur_nodes{
                let node_borrow = node.borrow();
                mx= std::cmp::max(node_borrow.val, mx);
            }
            
            ans.push(mx);
        }

        ans
    }
}
