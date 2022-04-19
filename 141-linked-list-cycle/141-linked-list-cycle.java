/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head == null){
            return false;
        }
        List<ListNode> nodeList = new LinkedList<>();
        while(head.next != null){
            if(nodeList.contains(head)){
                return true;
            }
            nodeList.add(head);
            head = head.next;
            
        }
        return false;
    }
}