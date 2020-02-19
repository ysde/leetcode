# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math

def get_num(l: ListNode):
    if l:
        return l.val
    else:
        return 0
    
def get_node(l: ListNode):
    if l:
        return l.next
    else: None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add(ll1: ListNode, ll2: ListNode, newList: ListNode, plus: bool):
            if ll1 is not None or ll2 is not None:
                tmp_sum = get_num(ll1) + get_num(ll2) + int(plus)
                newList.next = ListNode(tmp_sum % 10)
                add(get_node(ll1), get_node(ll2), newList.next, tmp_sum >= 10)
            elif plus:
                newList.next = ListNode(int(plus))
            
        first_sum = l1.val + l2.val
        first_node = ListNode(first_sum % 10)
        add(l1.next, l2.next, first_node, first_sum >= 10)
        
        
        return first_node