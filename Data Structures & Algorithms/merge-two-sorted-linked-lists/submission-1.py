# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()

        if list1 == None and list2 == None:
            return list1

        if list2 == None:
            return list1

        if list1 == None:
            return list2

        if list1.val > list2.val:
            dummy.next = list2
            list2 = list2.next
        else:
            dummy.next = list1
            list1 = list1.next

        current = dummy.next

        while list1 != None and list2 != None:
            if list1.val > list2.val:
                current.next = list2   # attach
                current = current.next # Advance attached node to our return list
                list2 = list2.next     # Advance list2
                                
            elif list1.val < list2.val:
                current.next = list1   
                current = current.next 
                list1 = list1.next     

            elif list1.val == list2.val:
                current.next = list1   
                current = current.next 
                list1 = list1.next  
        
        while list1 != None:
            current.next = list1   
            current = current.next 
            list1 = list1.next 


        while list2 != None:
            current.next = list2  
            current = current.next 
            list2 = list2.next

        return dummy.next







        
        

        