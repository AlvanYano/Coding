# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        prev = None
        current = head

        first = head
        cekVal = 999
        while current.next is not None:
            if ( cekVal == current.val):
                cekVal = current.val
                current = current.next
            else:
                first.next = current
                if prev is not None:
                    prev.next = first
                prev = first
                # print("first: ", first.val, "current: ", current.val)
                first = current
                cekVal = current.val
                current = current.next



            # first = current
            # while first.val is first.next.val:
            #     first = first.next
            # current = first.next
        
        return head

        

coba = ListNode(0, ListNode(0, ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))))
s = Solution()
result = s.deleteDuplicates(coba)
while result is not None:
    print(result.val)
    result = result.next

