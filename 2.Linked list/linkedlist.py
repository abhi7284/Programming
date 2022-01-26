

#single linkedlist node
class SNode:

    def __init__(self,data):

        self.data = data;
        self.next = None
        


class SingleLinkedList:

    def __init__(self):
        self.root = None

    def insert(self,data):
        
        new_node = SNode(data)

        if self.root == None:
            self.root = new_node
            return
        else:
            temp = self.root
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            return

    def find_middle(self):

        if self.root == None:
            print("Empty List!!")
            return

        elif self.root.next == None:
            return self.root.data
        else:

            sp = self.root
            fp = self.root.next
            
            while fp != None:
                if fp.next == None:
                    break
                fp = fp.next.next
                sp = sp.next
                
            return sp.data

        
    def delete_middle(self):

        if self.root == None:
            print("Empty list")
            return

        elif self.root.next == None:
            self.root = None
            return

        elif self.root.next.next == None:
            self.root = self.root.next
            return

        else:
            spp = self.root
            sp = self.root
            fp = self.root.next

            while fp != None:
                if fp.next == None:
                    spp.next = sp.next
                    break
                fp = fp.next.next
                spp = sp
                sp = sp.next

            spp.next = sp.next
            sp.next = None
            
            return

    def delete_all(self):
        if self.root == None:
            print("Already Empty List")
            return

        if self.root.next == None:
            self.root = None
            return
        
        while self.root.next == None:
            self.root.next  = self.root.next.next

        self.root = None

        

            

    def print_list(self):

        temp = self.root

        while temp != None:
            print(temp.data,end="->")
            temp = temp.next
        print()


llist = SingleLinkedList()

llist.insert(10)
llist.insert(20)
llist.insert(30)
llist.insert(40)
llist.insert(50)
llist.insert(60)
llist.insert(70)
llist.insert(80)


llist.print_list()

print(llist.find_middle())
llist.delete_middle()
llist.print_list()
llist.delete_all()




llist.print_list()
            
