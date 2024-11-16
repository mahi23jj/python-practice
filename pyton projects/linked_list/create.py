class node:
    def _init_(self, data):
        self.data = data
        self.next = None
class slinkedlist:
    def __init__(self):
        self.head = None
        self.tail=None
    def insert(self,value):
        new_node=node(value)
        new_node.next=None
        self.tail.next=new_node
        self.tail=new_node
    def insertml(self,value): # time coplexity is o(n) & space complexity o(1)
        new_node=node(value)
        cur=self.head
        index=0
        while index < 2:
            cur=cur.next
            index+=1
        nextnode=cur.next
        cur.next=new_node
        new_node.next=nextnode
    def tranverse(self):
            curr = self.head
            while curr.next:
                curr = curr.next
    def del_first(self):
        first=self.head
        if first.next==None:
            self.head=None
            self.tail=None
        else:    
            self.head=first.next
    def del_ind(self,ind): 
        index=0
        first=self.head
        while index<ind-1:
            first=first.next
            index+=1
        next_node=first.next    
        first.next=next_node.next   
    def del_last(self): # o(n)
        first=self.head
        while first is not None:
            if first.next==self.tail:
                break
            first=first.next
        first.next=None
        self.tail=first    
s=slinkedlist()
node1=node(1)
node2=node(2)
s.head=node1
s.head.next=node2
s.tail=node2    

