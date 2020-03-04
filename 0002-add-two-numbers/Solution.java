/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(0);
        ListNode final_res = res;
        int carry = 0;
        int output;
        while (l1 != null || l2 != null || carry != 0) {
            int val1 = 0;
            int val2 = 0;
            if (l1 != null) {
                val1 = l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                val2 = l2.val;
                l2 = l2.next;
            }
            output = (val1 + val2 + carry) % 10;
            carry = (int) (val1 + val2 + carry) / 10;
            res.next = new ListNode(output);
            res = res.next;
        }
        return final_res.next;
    }
}