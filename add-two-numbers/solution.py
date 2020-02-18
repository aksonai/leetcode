#Definition for singly-linked list.

class _Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next

class ListNode:

    def __init__(self):
        self._head = None
        # self._tail = None
        self._size = 0

    def push(self, e):
        self._head = _Node(e, self._head)
        self._size += 1

    def __str__(self):
        node = self._head
        to_print = str(node._element)
        while node._next:
            to_print += ' -> ' + str(node._next._element)
            node = node._next
        return to_print



l = ListNode()
l.push(4)
l.push(5)
l.push(3)

print(l)

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode: