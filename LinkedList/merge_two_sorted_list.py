# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = None
        while(list1 != None and list2 != None):
            if list1.val > list2.val :
                result_list = ListNode(list2.val, result_list)
                list2 = list2.next
            else :
                result_list = ListNode(list1.val, result_list)
                list1 = list1.next
        while(list1 != None) :
            result_list = ListNode(list1.val, result_list)
            list1 = list1.next
        while(list2 != None) :
            result_list = ListNode(list2.val, result_list)
            list2 = list2.next
        reverse_result = None
        while result_list != None :
            if reverse_result == None :
                reverse_result = ListNode(result_list.val, None)
            else :
                reverse_result = ListNode(result_list.val, reverse_result)
            result_list = result_list.next
        return reverse_result

