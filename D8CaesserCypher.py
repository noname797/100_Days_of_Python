import string
upper_case=[i for i in string.ascii_uppercase]
lower_case=[i for i in string.ascii_lowercase]

def encode():
    a=str(input("Type your message: \n"))
    b=int(input("Type the shift number:\n"))

    a_list=[i for i in a]

    for i in range(len(a_list)):
        if a_list[i] in upper_case:
            idx=upper_case.index(a_list[i])
            a_list[i]=upper_case[(idx+b)%25]
        elif a_list[i] in lower_case:
            idx=lower_case.index(a_list[i])
            a_list[i]=lower_case[(idx+b)%25]
    enc="".join(a_list)
    print(f"Here's the encoded result: {enc}")
def decode():
    a=str(input("Type your message: \n"))
    b=int(input("Type the shift number:\n"))

    a_list=[i for i in a]
    for i in range(len(a_list)):
        if a_list[i] in upper_case:
            idx=upper_case.index(a_list[i])
            a_list[i]=upper_case[(idx-b)%25]
        elif a_list[i] in lower_case:
            idx=lower_case.index(a_list[i])
            a_list[i]=lower_case[(idx-b)%25]
    dec="".join(a_list)
    print(f"Here's the encoded result: {dec}")


def playagain():
    in1=input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if in1=='yes':
        return True
    else:
         return False

    

if __name__=="__main__":
    run=True
    while run:
        in1=str(input("Type \"encode\" to encrypt and \"decode\" to decrpyt:\n"))
        if in1=="encode":
            encode()
            run=playagain()
        elif in1=="decode":
            decode()
            run=playagain()
        else:
            print("Wrong input try again.")
            continue