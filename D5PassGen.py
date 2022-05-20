from itertools import repeat
import string
import random

def intro():
    print("Welcome to the PyPassword Generator! ")
    a=int(input("How many characters would you like in your password?\n"))
    b=int(input("How many symbols would you like? \n"))
    c=int(input("How many numbers would you like?\n"))
    return a,b,c

def shuffle(a):
    '''Shuffles the elementss of the list.'''
    # or just use random.shuffle(x)
    for i in range(len(a)):
        idx=random.choice(range(0,len(a)))
        temp=a[i]
        a[i]=a[idx]
        a[idx]=temp
    return a

def passgen(a,b,c):
    upper_case=[i for i in string.ascii_uppercase]
    lower_case=[i for i in string.ascii_lowercase]
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','#','@','$','%','^','&','*','(',')','/','.']
    password=[]
    for i in range(b):
        password.append(random.choice(symbols))
    for i in range(c):
        password.append(random.choice(numbers))
    for i in range(a-b-c):
        password.append(random.choice(random.choice([upper_case,lower_case])))
    shuffled=shuffle(password)
    return "".join(shuffled)

if __name__=="__main__":
    repeat=True
    while repeat:
        a,b,c=intro()
        if a>=b+c:
            print(passgen(a,b,c))
            carry=str(input("Do you want to generate another password?\n"))
            if carry.lower()=="yes":
                print("\n"*10)
                continue
            else:
                repeat=False
        else:
            print("Wrong input. Try Again.")
            print("\n"*5)
            repeat=False


