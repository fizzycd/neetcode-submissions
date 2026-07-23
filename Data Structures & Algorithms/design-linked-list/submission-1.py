class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        old = self.head
        self.head = new
        new.next = old
        self.size += 1

        if not self.tail:
            self.tail = new

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        self.size += 1

        if not self.tail:
            self.head = self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        insert = ListNode(val)
        curr = self.head
        for _ in range(index-1):
            curr = curr.next
        insert.next = curr.next
        curr.next = insert
        self.size += 1
        return
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if self.size == 1:
            self.head = None
            self.tail = None
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
            if curr.next is None:
                self.tail = curr
        self.size -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)