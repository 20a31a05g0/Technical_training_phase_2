class Node:
    def __init__(self,value):
        self.prev=None
        self.data=value
        self.next=None
class Double:
    def insert(self,value,head):
        temp=head
        while temp.next!=None:
            temp=temp.next
        new_node=Node(value)
        new_node.prev=temp
        temp.next=new_node
    def print_list(self,head):
        temp=head
        while temp!=None:
            print(temp.data,end='->')
            temp=temp.next
        print()
    def print_reverse(self,head):
        temp=head
        while temp.next!=None:
            temp=temp.next
        while temp!=None:
            print(temp.data,end='<-')
            temp=temp.prev
        print()
    def remove(self,head):
        temp=head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
    def insert_at_pos(self,value,pos,head):
        temp=head
        prev=None
        while pos!=0:
            if prev==None:
                prev=Node(temp.data)
            else:
                new_node=Node(temp.data)
                self.insert(new_node,prev)
            temp=temp.next
            pos-=1
        new_node=Node(value)
        while prev.next!=None:
            prev=prev.next
        prev.next=new_node
        while prev!=None:
            new_node.prev=prev
            prev=prev.prev
        temp.prev=new_node
        new_node.next=temp
        return new_node
head=Node(10)
dl=Double()
dl.insert(20,head)
dl.insert(30,head)
dl.insert(40,head)
dl.insert(50,head)
dl.insert(60,head)
dl.print_list(head)
head=dl.insert_at_pos(25,2,head)
dl.print_list(head)
#dl.print_reverse(head)

            
