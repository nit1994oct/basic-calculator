import math
print("___Calculator___")

def sum(a,b):
    return a +b

def sub(a,b):
    if a>b :
        a-=b
        return a
    else:
        b=-a
        return b
def mul(a,b):
    return a*b

def div(a,b):
    q= a/b
    r= a%b
    print("\nThe quotient is :%s" %q)
    print("\nThe remainder is :%s" %r)


def sqr(a):
    return  math.sqrt(a)

while(True):
    print("\n\nChoose the operation you want to perform: ")
    print("\n\t1.Addition")
    print("\n\t2.Subtraction")
    print("\n\t3.Multiplication")
    print("\n\t4.Division")
    print("\n\t5.Square Root")
    print("\n\t6.EXIT")

    choice = int(input('>'))

    if choice==1:
        print("\n\nEnter the two numbers")
        num1 = int(input('>'))
        num2 = int(input('>'))
        s= sum(a,b)
        print("The sum is: %s" %s)

    elif choice==2:
        print("\n\nEnter the two numbers")
        num1 = int(input('>'))
        num2 = int(input('>'))
        m= sub(num1, num2)
        print("The difference is: %s" %s)

    elif choice==3:
        print("\n\nEnter the two numbers")
        num1 = int(input('>'))
        num2 = int(input('>'))
        p=  mul(num1, num2)
        print("The product is: %s" %s)

    elif choice==4:
        print("\n\nEnter the two numbers")
        num1 = int(input('>'))
        num2 = int(input('>'))
        div(num1,num2)

    elif choice==5:
        print("\n\nEnter the two numbers")
        num1 = int(input('>'))
        r = sqr(num1)   
        print("The square root is: %s" %r)

    else:
        print("You choose to exit.Bye...")
        break




        
        
     
    
    





    
    

