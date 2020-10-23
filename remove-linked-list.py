'''
Leetcode #203 Remove Linked List Element 

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution():
    def removeElements(self, head, val): 
    # output -> ListNode:
        current = head
        current.next = head
        prev = current
        
        while(prev.next != None):
            if(prev.next.val == val):
                prev.next = prev.next.next
            else:
                prev = prev.next
        return current.next

input_list = [1,2,6,3,4,5,6]
obj1 = Solution()
print(obj1.removeElements(input_list, 6))

##NOT SOLVED ---- KEEP WORKING ON THIS ONE. Working in Leetcode, but can't get it to work here