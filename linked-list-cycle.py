'''
Leetcode #141 Linked List Cycle

Given 'head', the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, 'pos' is used to denote the index of the node that tail's next pointer is connected to. Note that 'pos' is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''

# Input: head = [3,2,0,-4], pos = 1

# Output: true

# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution():
    def hasCycle(self, head): 
        #two pointers
        #second pointer moves twice as fast
        #if they eventually meet, that means there is a cycle (True)
        slower_pointer = head;
        faster_pointer = head;
        
        while faster_pointer and faster_pointer.next:
            faster_pointer = faster_pointer.next.next
            slower_pointer = slower_pointer.next
            
            if faster_pointer == slower_pointer:
                return True
        return False

input_list = [3, 2, 0, -4]
pos = 1
ob1 = Solution()
print(ob1.hasCycle(input_list, 1)) #should print True but is not working here b/c leetcode used an internal 'pos' that denotes the index of the node that tail's 'next' pointer is connected to. 'pos' is not passed as a parameter.