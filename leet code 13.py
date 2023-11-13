def reverse(head):
    prev = None
    cur = head
    nxt = head.next

    while cur != None:
        nxt = cur.next
        #change th direction of the nodes
        cur.next = prev
        #shifting the nodes
        prev = cur
        cur = nxt
    head = prev
    return head