MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def CashIn():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return 0.25*quarters+0.1*dimes+0.05*nickles+0.01*pennies


def check_resources(coffee):
    for i in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][i] > resources[i]:
            return False
    return True


def updater(coffee):
    global money, resources
    money += MENU[coffee]['cost']
    for i in MENU[coffee]['ingredients']:
        resources[i] -= MENU[coffee]['ingredients'][i]


def coffeemaker():
    gameon = True
    while gameon:
        int1 = input("What would you like? (espresso/latte/cappuccino): ")
        if int1 == 'report':
            for i in resources:
                print(f"{i} : {resources[i]}")
            print(f"Money: ${money}")

        elif int1 == 'off':
            gameon = False
            break

        else:
            check = check_resources(int1)
            if check:
                cash_in = CashIn()

                if cash_in >= MENU[int1]['cost']:
                    change = round(cash_in-MENU[int1]['cost'],2)
                    if change == 0:
                        print(f"Here is your {int1}. Enjoy!")
                        updater(int1)
                    else:
                        print(f"Here is ${change} in change.")
                        print(f"Here is your {int1}. Enjoy!")
                        updater(int1)
                else:
                    print("Money insufficient. Money refunded")

            else:
                items = []

                for i in MENU[int1]["ingredients"]:
                    if MENU[int1]["ingredients"][i] > resources[i]:
                        items.append(i)
                bruh = ", ".join(items)
                print(f"Sorry there is not enough {bruh}.")


if __name__ == "__main__":
    coffeemaker()

# TODO 1. Print report of all coffee machines.

# TODO 2. Check if all requirement exists.
