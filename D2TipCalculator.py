def tip():
    print("Welcome to the tip calculator")
    total=float(input("What was the total bill?\n"))
    count=float(input("How many people to split the bill ?\n"))
    percent=float(input("What percentage tip in?\n"))
    split="{:.2f}".format(total*(1+percent/100)/count) # Gives .0 at the end
    print(f"Each person has to pay $ {split}")

if __name__=="__main__":
    tip()