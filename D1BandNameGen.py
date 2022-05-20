def NameGen():

    print("Welcome to the Band Name Generator.\n")
    city=str(input("What's name of the city you grew up in?\n"))
    pet=str(input("What's your pet's name?\n"))
    return f"Your band name could be {city.capitalize()} {pet.capitalize()}"

if __name__=="__main__K":
    print(NameGen())


