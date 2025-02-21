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

use std::collections::HashSet;
use std::rc::Rc;
use core::cell::RefCell;

struct FindElements {
    values: HashSet<i32>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */

//TC: O(N) SC: O(N)
impl FindElements {

    fn dfs(r : Option<Rc<RefCell<TreeNode>>>, val: i32, values : & mut HashSet<i32>)
    {
        if let Some(rc_node) = &r 
        {
            let mut borrowed_node = rc_node.borrow_mut(); 
            borrowed_node.val = val;
            values.insert(val);
            Self::dfs(borrowed_node.left.clone(), val*2+1, values);
            Self::dfs(borrowed_node.right.clone(), val*2+2, values);
        }
    }

    fn new(root: Option<Rc<RefCell<TreeNode>>>) -> Self {
        let mut values = HashSet::new();
        Self::dfs(root, 0, &mut values);
        FindElements{
            values : values
        }
    }
    
    fn find(&self, target: i32) -> bool {
        return self.values.contains(&target);
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * let obj = FindElements::new(root);
 * let ret_1: bool = obj.find(target);
 */
