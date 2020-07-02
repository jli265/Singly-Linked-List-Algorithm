class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def buildList(seq):
    # seq is a list of objects.
    f = ListNode(None)
    c = f
    for obj in seq:
        c.next = ListNode(obj)
        c = c.next
    h, f.next = f.next, None
    return h

def reverseList(head):
    if not head or not head.next:
        return head
    h = reverseList(head.next)
    head.next.next = head
    head.next = None
    return h

h = buildList([1,2,3,4])
h = reverseList(h)