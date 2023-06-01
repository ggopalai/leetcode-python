/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    
    if (head.next == null) {
        return null
    }
    
    let dummy = new ListNode(0, head);
    
    let t = dummy;
    let x = dummy;
    
    for (let i = 0; i <= n; i++) {
        t = t.next;
    }
    
    while (t !== null) {
        t = t.next;
        x = x.next
    }
    
    // delete the required node.
    x.next = x.next.next;
    
    return dummy.next;
};