def playagain():
    inn=input("Enter 'yes' to play again. Else enter 'no'.\n" )
    if inn=="yes":
        return True
    else:
        return False

def calc():
    a=float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    cal_con=True
    while cal_con:
        c=input("Pick an operation: ")
        b=float(input("What's the next number?: "))

        if c=='+':
            result=a+b
            out="{:.2f}".format(result)
            print(f"{a} {c} {b} = {out}")
        elif c=='-':
            result=a-b
            out="{:.2f}".format(result)
            print(f"{a} {c} {b} = {out}")
        elif c=='/':
            result=a/b
            out="{:.2f}".format(result)
            print(f"{a} {c} {b} = {out}")
        elif c=='*':
            result=a*b
            out="{:.2f}".format(result)
            print(f"{a} {c} {b} = {out}")

        d=input(f"Type 'y' to continue calculating with {out}, or n to start a new calculations, or 'exit' to stop : ")
        if d=='y':
            a=result
            continue
        elif d=='n':
            cal_con=False
            calc()
        elif d=='exit':
            break

if __name__=="__main__":
    calc()




# ## Else
# def add(n1,n2):
#     return n1+n2

# def subtract(n1,n2):
#     return n1-n2

# def multiply(n1,n2):
#     return n1*n2

# def divide(n1,n2):
#     return n1/n2

# operations={'+':add,"-":subtract,"*":multiply,'/':divide}

# # function=operations['*']
# # function(2,3)

# num1=int(input("What's te first number?: "))
# num2=int(input("What's the second number?: "))

# for i in operations:
#     print(i)

# symbol=input("Pick an operation from the line above: ")


# func=operations[symbol]
# result=func(num1,num2)

# print(f"{num1} {symbol} {num2} = {result}")



# Or
def calculator(n1, n2, func):
    return func(n1,n2)