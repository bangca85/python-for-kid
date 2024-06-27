'''
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Create a dummy node to act as the starting point of the merged list
    dummy = ListNode()
    # Initialize a pointer to build the merged list
    current = dummy
    
    # Iterate while both lists have nodes
    while list1 and list2:
        # Compare the current nodes of both lists
        if list1.val < list2.val:
            # Attach the smaller node (list1) to the merged list
            current.next = list1
            # Move to the next node in list1
            list1 = list1.next
        else:
            # Attach the smaller node (list2) to the merged list
            current.next = list2
            # Move to the next node in list2
        list2 = list2.next
        # Move the current pointer to the next position in the merged list
        current = current.next
    
    # Attach any remaining nodes from list1 or list2
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    # The merged list starts at dummy.next
    return dummy.next

# Helper functions for testing
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def main():
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged_list = mergeTwoLists(list1, list2)
    print_linked_list(merged_list)  

if __name__ == "__main__":
    main()
