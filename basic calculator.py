def add(a,b):
    return a+b
def sub(a,b):
    return a-b 
def mul(a,b):
    return a*b
def div(a,b):
    b==0
    return a/b
def calculator():
    print("enter the choice 1,2,3,4")
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    c=int(input("enter the choice"))    
    a=eval(input("enter the number :"))
    b=eval(input("enter the number :"))
    if c==1:
        print("the addition of the two number is ",add(a,b))
    elif c==2:
        print("the sub of the two number is ",sub(a,b))
    elif c==3:
        print("the multiplication of the two number is ",mul(a,b))
    else:
        print("the division of the two number is ",div(a,b))
calculator()                      