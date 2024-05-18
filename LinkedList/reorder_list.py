# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseNode(self, node_list: ListNode) :
        new_node_list = None
        count = 0
        while(node_list != None):
            print('node_list.val', node_list.val)
            new_node_list = ListNode(node_list.val, new_node_list)
            node_list = node_list.next
            count += 1
        return count, new_node_list

    def dublicateNode(self, head: ListNode) :
        new_head = None
        while (head!=None):
            new_head = ListNode(head.val, new_head)
            head = head.next
        return new_head


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count, reverse_head = self.reverseNode(head)

        dublicate_head = self.dublicateNode(head)
        count, dublicate_head = self.reverseNode(dublicate_head)
        print('count', count)
        i = 1
        result_node = None
        temp = head
        prev_val = temp.val
        while (temp != None):
            print('i', i, prev_val)
            if i % 2 == 0 :
                temp.val = reverse_head.val
                reverse_head = reverse_head.next
            else :
                temp.val = dublicate_head.val
                dublicate_head = dublicate_head.next
            temp = temp.next
            i += 1

        