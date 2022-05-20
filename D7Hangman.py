from math import e
import random

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def playagain():
    int1=str(input("Enter yes to play again.\n"))
    if int1=='yes':
        gameon=True
        print("\n"*10)
        playgame(gameon)
    else:
        print("Good day.")
        gameon=False

def getpic(i):
    return HANGMANPICS[i]

def getword():
    return random.choice(words)

def findidx(a,b):
    """Finds the index of character b in list a"""
    idx=[]
    for i in range(len(a)):
        if a[i]==b:
            idx.append(i)
    return idx



def playgame(gameon=True):
    print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      ''')

    


    word=getword()
    chars=[i for i in word]
    u=["_" for i in chars]

    print(" ".join(u))
    life=6
    in_list=[]

    while gameon:
        inn=str(input("Guess a letter\n"))
    
        if len(inn)>1:
            print("Invalid Input. Try again.\n")
            continue
        if inn in in_list:
            print(f"You have already guessed {inn}")
            print(" ".join(u))
            print(getpic(6-life))
            continue
        if life==1:
            gameon=False
            print(getpic(6))
            print(f"You lose. The word is {word}")
            playagain()
            break
        if inn in chars:
            in_list.append(inn)
            idx=findidx(chars,inn)
            for i in idx:
                u[i]=inn
            print(" ".join(u))
        else:
            in_list.append(inn)
            print(" ".join(u))
            print(f"You guessed {inn}, that's not in the word.You lose a life.\n")
            life-=1
            print(getpic(6-life))
        
        if chars==u:
            gameon=False
            print("You win.")
            playagain()

    

if __name__=="__main__":
    playgame()
    