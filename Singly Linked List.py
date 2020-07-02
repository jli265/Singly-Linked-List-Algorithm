# define singly linked list
class ListNode(object):
    def __init__(self, value):
        self.next = None
        self.value = value


node1 = ListNode("H")
node2 = ListNode("E")
node1.next = node2


# traverse
def print_all_nodes(head):
    while head is not None:
        print(head.value)
        head = head.next


# search by index
def search_by_index(head, index):
    if head is None or index < 0:
        return None
    for move_times in range(index):
        head = head.next
        if not head:
            return None
    return head


# search by value
def search_by_value(head, value):
    if not head:
        return None
    current_node = head
    while current_node is not None:
        if current_node.value == value:
            return current_node
        current_node = current_node.next
    return None


# two nodes with same value in two memory addresses; not same object
n1, n2 = ListNode(1), ListNode(1)
print(n1 == n2)  # False


# define our own equality comparison
class ListNode(object):
    def __init__(self, value):
        self.next = None
        self.value = value

    def __eq__(self, other):
        return isinstance(other, ListNode) and self.value == other.value


# add to index v1
def add_to_index(head, index, value):
    if index == 0:
        new_head = ListNode(value)
        new_head.next = head
        return new_head
    else:
        prevNode = search_by_index(head, index - 1)
        if prevNode is None:
            return head
        new_node = ListNode(value)
        new_node.next = prevNode.next
        prevNode.next = new_node
        return head


# add to index v2
def add_to_index(head, index, value):
    fake_head = ListNode(None)
    fake_head.next = head
    insert_place = search_by_index(fake_head, index)
    if insert_place is None:
        return fake_head.next
    new_node = ListNode(value)
    new_node.next = insert_place.next
    insert_place.next = new_node
    return fake_head.next


# remove v1
def remove_from_index(head, index):
    if index == 0:
        return head.next
    else:
        prevNode = search_by_index(head, index - 1)
        if not prevNode or not prevNode.next:
            return head
        else:
            removeNode = prevNode.next
            prevNode.next = removeNode.next
            removeNode.next = None
            return head


# remove v2
def remove_from_index(head, index):
    fake_head = ListNode(None)
    fake_head.next = head
    remove_place = search_by_index(fake_head, index)
    if remove_place is None or remove_place.next is None:
        return fake_head.next
    remove_node = remove_place.next
    removeplace.next = remove_node.next
    remove_node.next = None
    return fake_head.next

