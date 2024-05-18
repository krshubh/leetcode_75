# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertNode(self, listNode: ListNode, resultNode: ListNode):
        if resultNode == None :
            return ListNode(listNode.val, None)
        else :
            temp_result_node = resultNode
            prev_result_node = None
            while(temp_result_node != None and temp_result_node.val > listNode.val):
                prev_result_node = temp_result_node
                temp_result_node = temp_result_node.next
            if prev_result_node != None :
                prev_result_node.next = ListNode(listNode.val, temp_result_node)
                return resultNode
            else:
                resultNode = ListNode(listNode.val, temp_result_node)
            return resultNode
    def reverse(self, node_list: ListNode):
        new_node_list = None
        while(node_list != None):
            new_node_list = ListNode(node_list.val, new_node_list)
            node_list = node_list.next
        return new_node_list

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result_llist = None
        flag = True
        temp = None
        while (flag):
            flag = False
            for i in range(len(lists)):
                if lists[i] != None :
                    result_llist = self.insertNode(lists[i], result_llist)
                    lists[i] = lists[i].next
                    flag = True
        result_llist = self.reverse(result_llist)
        return result_llist

        