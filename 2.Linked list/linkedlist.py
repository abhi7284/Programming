

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

    # NOT working
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

    # print reverse
    def print_reverse(self, temp):
        if temp:
            self.print_reverse(temp.next)
            print(temp.data, end = '<-')

        return

    #NOT working
    def reverse(self,i,j,k):

        # 0 element
        if self.root == None:
            return
        
        # 1 element
        elif self.root.next == None:
            return
        # 2 element
        elif self.root.next.next == None:
            temp = self.root.next
            self.root.next = None
            temp.next = self.root
            self.root = temp
            return
        else:
            if k.next:
                j.next = i
                self.reverse(j,k,k.next)
        self.root = k
        return

    #NOT working
    def is_palindrome(self,temp):

        if temp:
            self.is_palindrome(temp.next)
            if temp.data != self.data:
                print("NOT Palindrome!")
                return
        print("Palindrome")
        return
        
        
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


llist.print_list()
llist.print_reverse(llist.root)
print()
llist.print_list()
llist.is_palindrome(llist.root)
#llist.reverse(llist.root,llist.root.next,llist.root.next.next)

llist.print_list()            
