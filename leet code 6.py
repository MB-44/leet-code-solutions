# class Solution:
#     def isPalindrome(self, head: list):
#         if head==head:
#             return true
#         return false

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#          if head == None or head.next == None:
#             return head
#          prev, curr = None, head
#          while curr:
#                next_node = curr.next
#                curr.next = prev
#                prev = curr
#                curr = next_node
#          return prev