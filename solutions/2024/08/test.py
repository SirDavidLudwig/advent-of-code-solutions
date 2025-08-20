class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(ll):
    result = []
    while ll is not None:
        result.append(str(ll.val))
        ll = ll.next
    print(", ".join(result))

values = [1, 2, 3, 4, 5]
root = ListNode()
head = root
for x in values:
    head = head.next = ListNode(x)
print_list(root.next)
