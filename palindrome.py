#iterative method for number type
def is_palindrome(num):
    n1 = num
    n2 = 0
    while n1>0:
        t = n1%10
        n2 = n2*10 + t
        n1 = n1//10
        
    return num==n2

#recursion method for string type
def is_palindrome_rec(s):
    
    if len(s)== 0 or len(s)==1:
        return
    else:
        if s[0]!=s[-1]:
            return False
        is_palindrome_rec(s[1:])

    return True
       

num = input("Enter The Number: ")
print(is_palindrome(int(num)))
print(is_palindrome_rec(num))
