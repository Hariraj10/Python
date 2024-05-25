
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def modulo(a,b):
    return a%b

def main():
    print("Enter two numbers")
    a=int(input())
    b=int(input())
    print("Please select the operation to perform : +,-,*,/,%")
    c=input()
    if(c == '+'):
        print("Result: " + str(add(a,b)))
    elif(c == '-'):
        print("Result: " + str(sub(a,b)))
    elif(c == '*'):
        print("Result: " + str(mult(a,b)))
    elif(c == '/'):
        print("Result: " + str(div(a,b)))
    elif(c == '%'):
        print("Result: " + str(modulo(a,b)))
    else:
        print("Enter proper operation from the following : +,-,*,/,%")

main()