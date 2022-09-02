class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    list1 = []
    list2 = []

    trav = l1
    while trav != None:
        list1.append(trav.val)
        trav = trav.next

    trav = l2
    while trav != None:
        list2.append(trav.val)
        trav = trav.next

    print(list1)
    print(list2)


l1 = ListNode()
trav = l1
for i in range(4):
    trav = ListNode()
    trav.val = i
    trav = trav.next


l2 = ListNode()
trav = l2
for i in range(4):
    trav = ListNode()
    trav.val = i
    trav = trav.next

addTwoNumbers(l1, l2)
