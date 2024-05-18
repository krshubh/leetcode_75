# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        one_freq_list = head
        two_freq_list = head
        found = False
        while (one_freq_list!=None and two_freq_list!=None):
            if one_freq_list.next != None :
                one_freq_list = one_freq_list.next
            else :
                break
            if two_freq_list.next != None and two_freq_list.next.next != None :
                two_freq_list = two_freq_list.next.next
            else :
                break
            if one_freq_list == two_freq_list :
                found = True
                break
        return found

            
        