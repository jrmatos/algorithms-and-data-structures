# https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        my_str = str(head.val)

        while head.next != None:
            head = head.next
            my_str += str(head.val)

        return my_str == my_str[::-1]
