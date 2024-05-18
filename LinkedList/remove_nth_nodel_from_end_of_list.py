# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseNode(self, node_list: ListNode) :
        new_node_list = None
        while(node_list != None):
            new_node_list = ListNode(node_list.val, new_node_list)
            node_list = node_list.next
        return new_node_list

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.reverseNode(head)
        k = 1
        result_head = None
        while (head != None):
            if k != n :
                result_head = ListNode(head.val, result_head)
            k += 1
            head = head.next
        return result_head
