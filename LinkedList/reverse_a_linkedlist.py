# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_llist = head
        new_llist = None
        while(temp_llist):
            if new_llist != None :
                new_llist = ListNode(temp_llist.val, new_llist)
            else :
                new_llist = ListNode(temp_llist.val)
            temp_llist = temp_llist.next
        return new_llist
