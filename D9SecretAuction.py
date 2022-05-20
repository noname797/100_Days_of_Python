def secret_auction():
    auc_dic={}
    auctioning=True
    print("Welcome to the secret auction program.")
    while auctioning:
        name=str(input("What is your name?: "))
        bid=int(input("What's your bid?: $"))
        auc_dic[name]=bid
        others=str(input("Are there any other bidders? Type 'yes' or 'no'.\n"))
        if others=='no':
            auctioning=False
        else:
            pass # clear screen
    
    max_bid=0
    max_bidder=""

    for i in auc_dic.keys():
        if auc_dic[i]>=max_bid:
            max_bid=auc_dic[i]
            max_bidder=i
    
    print(f"The winner is {max_bidder} with a bid of ${max_bid}")
    




def playagain():
    inn=input("Enter 'yes' to play again. Else enter 'no'.\n" )
    if inn=="yes":
        return True
    else:
        return False

if __name__=="__main__":
    gameon=True
    while gameon:
        secret_auction()
        gameon=playagain()
        

