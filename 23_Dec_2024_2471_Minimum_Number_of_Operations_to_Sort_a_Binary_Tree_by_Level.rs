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
    //TC: O(NLOGN) SC: O(N)
    // Function to sort nodes and calculate the minimum number of swaps
    pub fn sort_nodes(cur_nodes: Vec<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut pairs: Vec<(i32, usize)> = cur_nodes
            .iter()
            .enumerate()
            .map(|(i, node)| (node.borrow().val, i))
            .collect();
        
        // Sort pairs by value
        pairs.sort_by_key(|&(val, _)| val);
        
        let n = pairs.len();
        let mut visited = vec![false; n];
        let mut swaps = 0;

        for i in 0..n {
            if visited[i] || pairs[i].1 == i {
                continue;
            }
            let mut cycle_count = 0;
            let mut j = i;

            // Count the size of the cycle
            while !visited[j] {
                visited[j] = true;
                j = pairs[j].1;
                cycle_count += 1;
            }

            if cycle_count > 1 {
                swaps += cycle_count - 1;
            }
        }

        swaps
    }

    pub fn minimum_operations(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut q = VecDeque::new();
        if let Some(node) = root {
            q.push_back(node);
        }

        let mut ans = 0;

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

            ans += Self::sort_nodes(cur_nodes);
        }

        ans
    }
}
