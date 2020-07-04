class Node():
    def __init__(self, val):
        self.value = val
        self.next = None
        self.flag = False


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    # insert at the beginning, O(1)
    def push(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node

    # print the LL
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.value, end=" ")
            temp = temp.next

    def detectALoop(self):
        s = set()
        temp = self.head
        while(temp):
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next

        return False

    def detectLoopWithoutSet(self):
        temp = self.head
        while(temp):
            if temp.flag:
                return True
            temp.flag = True
            temp = temp.next
        return False

    def detectLoopFloyd(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False

    def sizeLoop(self):
        slow_p = self.head
        fast_p = self.head
        flag = 0
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                flag = 1
                break
        if not flag:
            return 0
        fast_p = fast_p.next
        counter = 1
        while(fast_p != slow_p):
            fast_p = fast_p.next
            counter += 1
        return counter


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head


if(llist.detectLoopFloyd()):
    print("Loop found")
else:
    print("No Loop ")

print(llist.sizeLoop())
