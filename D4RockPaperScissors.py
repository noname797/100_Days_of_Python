import random

def playagain():
    int4=input("Enter \"yes\" to play again.\n")
    if int4=="yes":
        print("\n"*10)
        playgame(True)
    else:
        print("Good day.")


def printascii(choice):
    if choice==0:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif choice==1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    elif choice==2:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        

def computerchoice():
    return random.randint(0,2)

def win(c1,c2):
    if (c1==0 and c2==2) or (c1==1 and c2==0) or (c1==2 and c2==1) :
        return 0
    elif c1==c2:
        return 1
    else:
        return 2



def playgame(gameon=True):
    gameon=True
    while gameon:
        int1=int(input("What do you choose? Type 0 for rock,1 for paper or 2 for scissors.\n"))
        c_choice=computerchoice()
        if int1 in range(3):
            printascii(int1)
            print("Computer chose: \n")
            printascii(c_choice)
            if win(int1,c_choice)==0:
                print("You win.")
                gameon=False
                playagain()
            elif win(int1,c_choice)==1:
                print("Game Draw.")
                gameon=False
                playagain()
            else:
                print("Computer Win you lose.")
                gameon=False
                playagain()
        else:
            print("Invalid input.")
            gameon=False
            playagain()

if __name__=="__main__":
    playgame(True)


