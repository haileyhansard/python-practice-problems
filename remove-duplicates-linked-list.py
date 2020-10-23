#From unit assessment 
# on CodeSignal

#Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. Your function should return a reference to the head of the updated linked list.

#Example:
#Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
#Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
#Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.


#My solution:
#Input: Linked list of integers
    #Given Unsorted linked list
    #Use hashtable to keep track of elements
    #Remove duplicate nodes by pointing to the next node if it is already in the cache
#Output: return a reference to the head of the updated linked list

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def condense_linked_list(node):
    cache = []
    if node is None:
        return
    cache.append(node.value)
    head = node
    
    while node.next is not None:
        if node.next.value not in cache:
            cache.append(node.next.value)
            node = node.next
            
        else:
            node.next = node.next.next
            
    return head
