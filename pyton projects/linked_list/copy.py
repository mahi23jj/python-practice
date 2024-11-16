class Node:
    def __init__(self, x: int, next: 'Node' = None):
        self.val = int(x)
        self.next = next
        #self.random = random
class slinkedlist:
    def __init__(self):
        self.head = None
    def print_list(self,current):
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")    
    def copyList(self):
        new=Node(self.head.val)
        new.next=self.head.next
        sec=self.head.next
        vas=sec.next
        while vas:
            s=Node(vas.val)
            s.next=vas
            vas=vas.next
        return new  

X=Node(7)
y=Node(13)
z=Node(3)
l=Node(9)
s=slinkedlist()
s.head=X
X.next=y
y.next=z
z.next=l
l.next=None

s.print_list(s.copyList())

