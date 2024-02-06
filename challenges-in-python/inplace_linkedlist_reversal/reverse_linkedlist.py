# Solving the "Reverse Linked List" Challenge
# Challenge Description:
# Given the head of a singly linked list, reverse the list and return the reversed list.

# Approach:
# Iteratively change the next pointers of each node to point to the previous node. 
# You need to handle the new connections and the next node's reference before 
# changing the next pointer.

# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Function to convert list to linked list
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for i in range(0, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next
    return dummy.next

# Function to convert linked list to list
def linked_list_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.value)
        current = current.next
    return lst

def reverse_linked_list(head):
    prev, current = None, head
    while current:
        next_temp = current.next # Save the next node
        current.next = prev # Reverse the link
        prev = current # Move prev up
        current = next_temp # Move current up
    return prev # New head of the reversed list

# The Function to reverse a list
def reverse_list(lst):
    head = list_to_linked_list(lst)
    reversed_head = reverse_linked_list(head)
    return linked_list_to_list(reversed_head)


# Testing the function
def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_list([]) == []
    assert reverse_list([1]) == [1]

test_reverse_list()