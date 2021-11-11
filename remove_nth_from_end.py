class ListNode:
    def __init__(self, val, next = None):
      self.val = val
      self.next = next

def createListNode(arr):
  p, l = None, None
  for d in arr:
    if l is None:
      l = ListNode(d)
      p = l
    else:
      p.next = ListNode(d)
      p = p.next
  return l

def printListNode(head):
  k = head
  arr = []
  while k is not None:
    arr.append(k.val)
    k = k.next
  print(arr)

nd = createListNode(['1','2','3','4','5'])

printListNode(nd)

# 双指针
def remove_nth_from_end(head, n):
  k, target = head, head
  while (k.next is not None):
    k = k.next
    if n == 0:
      target = target.next
    else:
      n = n - 1
  print(n)
  if (n > 0):
    return head.next
  if (target.next is not None):
    target.next = target.next.next
  else:
    target.next = None
  
  return head

h = remove_nth_from_end(nd, )

printListNode(h)