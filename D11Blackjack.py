import random

def playagain():
    inn=input("Enter 'yes' to play again. Else enter 'no' \n")
    if inn=='yes':
        return True
    else:
        return False

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_cards(m):
    hand=[]
    for i in range(m):
        hand.append(random.choice(cards))
    return hand



def blackjack():

    computer_hand=deal_cards(2)
    your_hand=deal_cards(2)
    
    while sum(computer_hand)<17:
        computer_hand.append(random.choice(cards))

    print(f"Your cards: {your_hand}, current score: {sum(your_hand)}")
    print(f"computer's first card: {computer_hand[0]}")

    if 11 in computer_hand and sum(computer_hand)>21:
        idx=computer_hand.index(11)
        computer_hand[idx]=1

    draw=True
    while draw:
        inn=input("Type 'y' to get another card, type 'n' to pass: ")

        if inn=='y':
            your_hand.append(random.choice(cards))
            print(f"Your cards: {your_hand}, current score: {sum(your_hand)}")
        else:
            draw=False
    
    print(f"Your final hand: {your_hand}, final score: {sum(your_hand)}")
    print(f"computer's final card: {computer_hand}, final score: {sum(computer_hand)}")

    if (sum(your_hand)>21 and sum(computer_hand)>21) or (sum(your_hand) == sum(computer_hand)):
        print("Draw.")

    elif sum(your_hand)<=21 and sum(computer_hand)>21:
        print("You win.")

    elif sum(your_hand)>21 or sum(your_hand)<sum(computer_hand):
        print("You lose")

    else:
        print("You Win.")

if __name__=="__main__":
    gameon=True
    while gameon:
        blackjack()
        gameon=playagain()
