class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class ll:
    def insert(self,value,head):
        if head==None:
            head=node(value)
        else:
            temp=head
            while temp.next!=None:
                temp=temp.next
            new_node=node(value)
            temp.next=new_node
    def printll(self,head):
        temp=head
        if temp==None:
            print('list is empty')
        else:
            while temp!=None:
                print(temp.data,'->',end='')
                temp=temp.next
    def remove(self,value,head):
        temp=head
        if temp==None:
            print('list is empty')
        else:
            prev=None
            cur=None
            while temp!=None:
                if temp.data==value:
                    cur=temp.next
                    break
                else:    
                    new_node=node(temp.data)
                    if prev==None:
                        prev=new_node
                    else:
                        pre=prev
                        while pre.next!=None:
                            pre=pre.next
                        prev.next=new_node
                temp=temp.next
            if cur==None:
                print('element not found')
            else:
                prev.next=cur
            return prev
    def add_at_pos(self,value,pos,head):
        temp=head
        prev=None
        while pos!=0:
            if prev==None:
                prev=node(temp.data)
            else:
                prev.next=node(temp.data)
            temp=temp.next
            pos-=1
        prev.next=node(value)
        prev.next=temp
        return prev

    def reverse(self,head):
        temp=head
        node1=None
        node2=None
        while temp!=None:
            node2=node(temp.data)
            node2.next=node1
            node1=node2
            temp=temp.next
        return node1
            
            
            
            

l=ll()
head=node(10)
l.insert(20,head)
l.insert(30,head)
l.insert(40,head)
l.printll(head)
print()
head=l.reverse(head)
l.printll(head)
print()
head=l.reverse(head)
l.printll(head)
print()
head=l.add_at_pos(100,2,head)
l.printll(head)
print()

