use std::borrow::BorrowMut;

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl From<Vec<i32>> for ListNode {
    fn from(items: Vec<i32>) -> Self {
        let Some(_) = items.first() else {
            panic!("empty linked list");
        };

        let mut head = None;
        for i in items.into_iter().rev() {
            head = Some(Box::new(ListNode { val: i, next: head }))
        }
        *head.unwrap()
    }
}

// Impossible since we need to keep track of separator as mut reference and mutate later
// node that is smaller than x => 2 mutable reference for a Box (not possible)
// pub fn partition(head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
//     let head = head?;
//     let mut separator = &ListNode {
//         val: 0,
//         next: Some(head),
//     };
//     loop {
//         if let Some(next_node) = &separator.next {
//             if next_node.val >= x {
//                 break;
//             }
//             separator = next_node;
//             continue;
//         };
//         break;
//     }
//     let curr = separator.next.as_mut();
//     None
// }

pub fn partition(head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
    let mut curr = head?;
    let mut left = ListNode::new(0);
    let mut right = ListNode::new(0);
    let mut l_head = &mut left;
    let mut r_head = &mut right;
    loop {
        if curr.val >= x {
            r_head.next = Some(Box::new(ListNode::new(curr.val)));
            r_head = r_head.next.as_mut()?;
        } else {
            l_head.next = Some(Box::new(ListNode::new(curr.val)));
            l_head = l_head.next.as_mut()?;
        }
        match curr.next {
            None => {
                break;
            }
            Some(next) => curr = next,
        }
    }
    l_head.next = right.next;
    left.next
}

#[cfg(test)]
mod tests {
    use crate::partitionList_86::{partition, ListNode};

    // Test how derive Eq works for recursive struct
    #[test]
    fn test0() {
        assert_eq!(
            ListNode::from([1, 2, 2, 4, 3, 5].to_vec()),
            ListNode::from([1, 2, 2, 4, 3, 5].to_vec()),
        );
    }

    #[test]
    fn test1() {
        assert_eq!(
            partition(Some(Box::new([1, 4, 3, 2, 5, 2].to_vec().into())), 3),
            Some(Box::new([1, 2, 2, 4, 3, 5].to_vec().into()))
        );
    }

    #[test]
    fn test2() {
        assert_eq!(
            partition(Some(Box::new([2, 1].to_vec().into())), 2),
            Some(Box::new([1, 2].to_vec().into()))
        );
    }
}
