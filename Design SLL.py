class _ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = None
        self._size = 0
        self._tail = None

    def _get(self, index):
        node = self._head
        for _ in range(index):
            node = node.next
        return node

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self._size:
            return -1
        return self._get(index).val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        if self._size == 0:
            self._head = _ListNode(val)
            self._tail = self._head
        else:
            new_head = _ListNode(val)
            new_head.next = self._head
            self._head = new_head
        self._size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self._size == 0:
            self._head = self._tail = _ListNode(val)
        else:
            self._tail.next = _ListNode(val)
            self._tail = self._tail.next
        self._size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self._size:
            return None
        if index == 0:
            self.addAtHead(val)
        elif index == self._size:
            self.addAtTail(val)
        else:
            node = self._get(index - 1)
            new_node = _ListNode(val)
            new_node.next = node.next
            node.next = new_node
        self._size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self._size:
            return None
        if index == 0:
            new_head = self._head.next
            self._head.next = None
            self._head = new_head
            if not self._head:
                self._tail = None
        else:
            node = self._get(index - 1)
            remove_node = node.next
            node.next = remove_node.next
            remove_node.next = None
            if index == self._size - 1:
                self._tail = node
        self._size -= 1


# Your Solution object will be instantiated and called as such:
# obj = Solution()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


linkedList = Solution();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  # linked list becomes 1->2->3
linkedList.get(1);  # returns 2
linkedList.deleteAtIndex(1);  # now the linked list is 1->3
linkedList.get(1);  # returns 3