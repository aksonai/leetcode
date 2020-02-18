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

    def reverse(self):
        new_list_node = ListNode()
        curr = self._head
        while curr:
            new_list_node.push(curr._element)
            curr = curr._next
        return new_list_node

    def __str__(self):
        node = self._head
        to_print = str(node._element)
        while node._next:
            to_print += ' -> ' + str(node._next._element)
            node = node._next
        return to_print


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = ListNode()
        n1 = l1._head
        n2 = l2._head
        carry = 0
        while n1 or n2:
            if n1:
                el1 = n1._element
                n1 = n1._next
            else:
                el1 = 0
            if n2:
                el2 = n2._element
                n2 = n2._next
            else:
                el2 = 0
            sum.push((el1 + el2) % 10 + carry)
            carry = (el1 + el2) // 10
        return sum.reverse()


if __name__ == '__main__':
    
    l1 = ListNode()
    l1.push(1)
    l1.push(3)
    l1.push(4)
    l1.push(2)

    l2 = ListNode()
    l2.push(4)
    l2.push(6)
    l2.push(5)

    sol = Solution()
    print(l1)
    print(l2)
    print(sol.addTwoNumbers(l1, l2))