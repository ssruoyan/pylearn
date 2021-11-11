# 两个链表表示两个数字的【倒序】，相加两个数字得到结果的倒序链表表示。

class ListNode:
    def __init__(self, value=0, next=None):
        self.next = next
        self.value = value

    def add(self, value):
        self.next = ListNode(value)
        return self.next

    def to_num(self):
        ln = self
        num = 0
        multi = 0
        while ln is not None:
            num = num + ln.value * pow(10, multi)
            multi = multi + 1
            ln = ln.next
        return num


def add_two_num(l1: ListNode, l2: ListNode):
    l3 = None
    nxt = None
    forward = 0
    while l1 is not None or l2 is not None:
        if l1 is not None:
            forward += l1.value
            l1 = l1.next
        if l2 is not None:
            forward += l2.value
            l2 = l2.next
        if l3 is None:
            l3 = ListNode(forward % 10)
            nxt = l3
        else:
            nxt.next = ListNode(forward % 10)
            nxt = nxt.next
        forward = forward // 10
    if forward > 0:
        nxt.next = ListNode(forward)
    return l3


num1 = ListNode(2)
num1.add(4).add(3)
num2 = ListNode(5)
num2.add(6).add(4)

# add_two_num(num1, num2)
print(add_two_num(num1, num2).to_num())
