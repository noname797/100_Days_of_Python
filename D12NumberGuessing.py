import random

def playagain():
    if input("Enter 'yes' to play again, else play 'no': \n")=='yes':
        print("\n"*10)
        return True
    return False

count=5

def playgame():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    global number
    number=random.randint(1,100)
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
    global count
    if difficulty=='hard':
        count=5
        play()
    elif difficulty=='easy':
        count=10
        play()
    else:
        print("Wrong input.")



def play():
    global count
    guessing=True
    while guessing and count>0:
        print(f"You have {count} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))
        if guess>number:
            print("Too high.\n Guess again.")
            count-=1
            if count<=0:
                print(f"You lose. The number is {number}")
        elif guess<number:
            print("Too low.\n Guess again.")
            count-=1
            if count<=0:
                print(f"You lose. The number is {number}")
        elif guess==number:
            print(f"You got it! The answer is {number}")
            break
    

    
    



if __name__=="__main__":
    gameon=True
    while gameon:
        playgame()
        gameon=playagain()