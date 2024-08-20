def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        previous = None
        current = head
        
        while head is not None:
            next = head.next
            head.next = previous
            previous = current
            current = next
            head = next
        return previous
        
# Time Complexity : O(n), n = length of linked list
# Space Complexity: O(1)