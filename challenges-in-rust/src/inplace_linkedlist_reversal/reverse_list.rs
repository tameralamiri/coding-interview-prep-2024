// Solving the "Reverse Linked List" Challenge
// Problem Statement
// Given the head of a singly linked list, reverse the list, and return the reversed list.

// Example 1:
// Input: head = [1,2,3,4,5]
// Output: [5,4,3,2,1]

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    fn new(val: i32) -> Self {
        ListNode {
            val,
            next: None,
        }
    }
}

//  convert a vector to a linked list
fn vec_to_linked_list(vec: Vec<i32>) -> Option<Box<ListNode>> {
    let mut current = None;
    for &val in vec.iter().rev() {
        let mut new_node = ListNode::new(val);
        new_node.next = current;
        current = Some(Box::new(new_node));
    }
    current
}

// convert a linked list to a vector
fn linked_list_to_vec(list: Option<Box<ListNode>>) -> Vec<i32> {
    let mut current = list;
    let mut vec = vec![];
    while let Some(node) = current {
        vec.push(node.val);
        current = node.next;
    }
    vec
}

// reverse a linked list
fn reverse_linked_list(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut prev = None;
    while let Some(mut node) = head {
        let next = node.next.take();
        node.next = prev.take();
        prev = Some(node);
        head = next;
    }
    prev

}

// public function to reverse the vector of values using the helper functions
pub fn reverse_list(vec: Vec<i32>) -> Vec<i32> {
    let list = vec_to_linked_list(vec);
    let reversed_list = reverse_linked_list(list);
    linked_list_to_vec(reversed_list)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_reverse_list() {
        assert_eq!(reverse_list(vec![1, 2, 3, 4, 5]), vec![5, 4, 3, 2, 1]);
        assert_eq!(reverse_list(vec![1, 2]), vec![2, 1]);
        assert_eq!(reverse_list(vec![1]), vec![1]);
        assert_eq!(reverse_list(vec![]), vec![]);
    }
}