# 单链表实现

class SLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    # 判断是否为空
    def is_empty(self):
        return self.size == 0

    # 插入
    def insert(self, pos, data):
        if pos >= self.size:
            return self.append(data)
        if pos <= 0:
            return self.prepend(data)
        root = self.head
        i = 0
        while i < pos - 1 and root is not None:
            root = root.next
            i += 1
        node = SLinkedListNode(data)
        node.next = root.next
        root.next = node
        self.size += 1
        return node

    # 移除
    def remove(self, pos):
        if pos >= self.size or pos < 0:
            return False

        # if remove head node, set self.head
        if (pos == 0):
            self.head = self.head.next
        i = 0
        root = self.head
        pre = None
        while i < pos:
            pre = root
            root = root.next
        pre.next = root.next
        self.size -= 1

        # if remove tail node, set self.tail
        if pos == self.size:
            self.tail = pre.next
        return root

    # 从后面插入^▽^
    def append(self, data):
        tail = SLinkedListNode(data)
        if self.tail is not None:
            self.tail.next = tail

        self.tail = tail
        if self.head is None:
            self.head = tail
        self.size += 1
        return self.size

    # 从前面插入^_^
    def prepend(self, data):
        head = SLinkedListNode(data)
        if self.head is not None:
            head.next = self.head

        self.head = head
        if self.tail is None:
            self.tail = head
        self.size += 1
        return self.size

    # 查找
    def find(self, pos):
        if pos >= self.size or pos < 0:
            return None

        i = 0
        node = self.head
        while i < pos:
            node = node.next
            i += 1
        return node

    # 遍历整个链表
    def travel(self):
        arr = []
        node = self.head
        while node is not None:
            arr.append(node.value)
            node = node.next
        print(arr)

    # 反转链表（迭代）
    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        self.tail = self.head
        self.head = prev

    def reverse1(self):
        head = self.tail
        tail = self.head
        while head != tail:
            head.next = tail
            tail = tail.next
        self.tail.next = None
