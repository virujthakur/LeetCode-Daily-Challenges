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

// TC: O(N) SC: O(N)
impl Solution {
    pub fn reverse_odd_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if root.is_none() {
            return root;
        }

        let root = root.unwrap();
        let mut q = VecDeque::new();
        q.push_back(root.clone());
        let mut level = 0;

        while !q.is_empty() {
            let sz = q.len();
            let mut current_level = Vec::new();

            // Collect nodes for the current level
            for _ in 0..sz {
                let node = q.pop_front().unwrap();
                current_level.push(node.clone());

                let node_ref = node.borrow();
                if let Some(left) = &node_ref.left {
                    q.push_back(left.clone());
                }
                if let Some(right) = &node_ref.right {
                    q.push_back(right.clone());
                }
            }

            // Reverse values if it's an odd level
            if level % 2 == 1 {
                let values: Vec<i32> = current_level.iter().map(|node| node.borrow().val).collect();
                for (i, node) in current_level.iter().enumerate() {
                    node.borrow_mut().val = values[values.len() - 1 - i];
                }
            }

            level += 1;
        }

        Some(root)
    }
}
