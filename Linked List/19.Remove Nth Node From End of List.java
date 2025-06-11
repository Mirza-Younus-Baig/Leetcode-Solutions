
/*Definition for Singly Linked List
class ListNode {
    int val;
    ListNode next;

    ListNode() {
        val = 0;
        next = null;
    }

    ListNode(int data1) {
        val = data1;
        next = null;
    }

    ListNode(int data1, ListNode next1) {
        val = data1;
        next = next1;
    }
}
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // for brute force approach refer Cpp Solution
        ListNode fast = new ListNode();
        ListNode slow = new ListNode();

        fast = slow = head;

        if(head.next == null){
            head = null;
            return head;
        }

        for(int i = 0; i< n ; i++)
        {
            fast = fast.next;
        }
        if(fast == null){
            head = head.next;
        }
        else{
        while(fast.next != null){
            slow = slow.next;
            fast = fast.next;
        }
        slow.next = slow.next.next;
}
        return head;

    }
}

// Add toString() to ListNode and main() to Solution:

// Assuming ListNode is accessible here (if not, move this into the ListNode class definition)
class ListNode {
    int val;
    ListNode next;

    ListNode() {
        val = 0;
        next = null;
    }

    ListNode(int data1) {
        val = data1;
        next = null;
    }

    ListNode(int data1, ListNode next1) {
        val = data1;
        next = next1;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        ListNode current = this;
        while (current != null) {
            sb.append(current.val).append(" -> ");
            current = current.next;
        }
        sb.append("null");
        return sb.toString();
    }
}

class Main {
    public static void main(String[] args) {
        // Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        int n = 2;

        Solution sol = new Solution();
        System.out.println("Original list: " + head);
        ListNode updatedHead = sol.removeNthFromEnd(head, n);
        System.out.println("After removing " + n + "th node from end: " + updatedHead);
    }
}