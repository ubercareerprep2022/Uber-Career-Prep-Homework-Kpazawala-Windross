class Linkedlist:
    #public

    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def push(self, value):
        self.head = self.Node(value, self.head)
        if self.tail == None:
            self.tail = self.head
    def pop(self):
        if(self.size() > 1):
            tmp = self.tail.data
            h = self.head
            while h:
                if h.next.next == None:
                    h.next = None
                    self.tail = h
                    break
                h = h.next
            return tmp

    def insert(self, uint, index):
        h = self.head
        i = 0
        while h:
            if index == 0:
                tmp = h
                self.head = self.Node(uint, tmp)
                break
            elif(i == index-1):
                tmp = h.next
                h.next = self.Node(uint, tmp)
                break 

            i += 1
            h = h.next
    def remove(self, index):
        if(self.size() > 1):
            h = self.head
            i = 0
            while h:
                if i == index-1:
                    if h.next != None:
                        h.next = h.next.next
                        break
                    else: 
                        h.next = None
                else: 
                    h = h.next
                    i += 1
    
    def elementAt(self, index):
        if(self.size() > 1):
            h = self.head
            i = 0
            while h:
                if i == index-1:
                    if h.next != None:
                        return h.next
                    else: 
                        h.next = None
                        return h.next
                else: 
                    h = h.next
                    i += 1
        else: 
            return None
    def size(self):
        h = self.head
        i = 0
        while h:
            if h == None:
                break
            else: 
                h = h.next
                i += 1
        return i

    def printList(self):
        h = self.head
        while(h != None):
            print(h.data)
            h = h.next

    #private
    class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next

def testPushBackAddsOneNode():
    print("testPushBackAddsOneNode")
    llist = Linkedlist()
    llist.push(1)
    llist.printList()
    print()

    del llist
    
def testPopBackRemovesCorrectNode():
    print("testPopBackRemovesCorrectNode")
    llist = Linkedlist()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)

    llist.pop()
    llist.printList()
    print()
    
    del llist

def testEraseRemovesCorrectNode():
    print("testEraseRemovesCorrectNode")
    llist = Linkedlist()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)

    llist.remove(1)
    llist.printList()
    print()

    del llist

def testEraseDoesNothingIfNoNode():
    print("testEraseDoesNothingIfNoNode")
    llist = Linkedlist()

    llist.remove(0)
    llist.printList()
    print()

    del llist

def testElementAtReturnNode():
    print("testElementAtReturnNode")
    llist = Linkedlist()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)

    print("Pointer: ", llist.elementAt(1), "Value: ", llist.elementAt(1).data)
    print()
    
    del llist

def testElementAtReturnsNoNodeIfIndexDoesNotExist():
    print("testElementAtReturnsNoNodeIfIndexDoesNotExist")
    llist = Linkedlist()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)

    print("Pointer: ", llist.elementAt(5))
    print()

    del llist

def testSizeReturnsCorrectSize():
    print("testSizeReturnsCorrectSize")
    llist = Linkedlist()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)

    print(llist.size())
    print()
    
    del llist



if __name__ == "__main__":
    testPushBackAddsOneNode()
    testPopBackRemovesCorrectNode()
    testEraseRemovesCorrectNode()
    testEraseDoesNothingIfNoNode()
    testElementAtReturnNode()
    testElementAtReturnsNoNodeIfIndexDoesNotExist()
    testSizeReturnsCorrectSize()

