from Part4 import Linkedlist
class recLinkedList:
    
    def __init__(self, llist):
        self.head = llist.head
        self.list = Linkedlist()
        recLinkedList.recur(self.list, self.head)

    def recur(rev_list, head):
        if head == None:
            return 0
        else:
            recLinkedList.recur(rev_list, head.next)
            rev_list.push(head.data)

        return rev_list

def printL(head):
    if head == None:
        return 0
    else:
        printL(head.next)
        print(head.data)



if __name__ == "__main__":
    llist = Linkedlist()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    print(llist.head)

    printL(recLinkedList(llist).head)
