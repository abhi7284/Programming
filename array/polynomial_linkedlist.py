

class Node:
    def __init__(self,c,e):
        self.c = c
        self.e = e
        self.next = None


def polyAddition(A,B):
    
    p1 = A
    p2 = B
    while p1:
        print(p1.c,'x^',p1.e, end=" ")
        p1=p1.next
    print()
    
    while p2:
        print(p2.c,'x^',p2.e,end=' ')
        p2 = p2.next
    p1 = A
    p2 = B
    print()
    print('----------')

    while(p1!=None or p2!=None):
        if(p1== None):
            while p2:
                print(p2.c,'x^',p2.e,end=' ')
                p2 = p2.next
            break
        
        elif (p2 == None):
            while p1:
                print(p1.c,'x^',p1.e,end=' ')
                p1 = p1.next
            break;

        elif(p1.e == p2.e):
            print((p1.c+p2.c),"x^",p1.e,end=' ')
            p1 = p1.next
            p2 = p2.next

        elif (p1.e > p2.e):
            print(p1.c,"x^",p1.c,end=' ')
            p1 = p1.next

        else :
            print(p2.c,"x^",p2.c,end=' ')
            p2 = p2.next


a = Node(3,1)


b = Node(2,2)
b.next = Node(1,1)
b.next.next=Node(5,0)

polyAddition(a,b)
