
# To check for ASCII ART visit ascii.co.uk/art

def playagain():
    int4=input("Enter \"yes\" to play again.\n")
    if int4=="yes":
        print("\n"*10)
        playgame(True)
    else:
        print("Good day.")


def playgame(gameon=True):
    while gameon: 
        print("Welcome to Treasure Island.")
        print("Your mission is to find the treasure.")
        int1=input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
        if int1 == "right":
            print("Game Over. Cz you got hit by a car.")
            gameon=False
            playagain()
        else:
            int2=input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
            if int2=="swim":
                print("Game Over. Cz a shark ate you.")
                gameon=False
                playagain()
            else:
                int3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
                if int3=="blue":
                    print("You entered a room of beast. Game Over")
                    gameon=False
                    playagain()
                elif int3=="red":
                    print("You dead. Game over")
                    gameon=False
                    playagain()
                elif int3=="Yellow":
                    print("You win")
                    gameon=False
                    playagain()
                else:
                    print("The door doesn't exists.")
                    gameon=False
                    playagain()

if __name__=="__main__":
    playgame(True)

