from typing import AnyStr
import re
# coffe machine
# 7-25-25

STATE = True
ingredeints_in_tank = {"water":10000, "milk":1, "coffee":100000}

# i did it like this bc i wanted a way to ref the menu item and have its reqs right there i also wanted them to be less memoru intesne so i made them immutable

# oh boy
recipes = {
    "espresso": {"water": 50, "milk": 0, "coffee": 50},
    "americano": {"water": 100, "milk": 0, "coffee": 50},
    "latte": {"water": 50, "milk": 100, "coffee": 50}
}

price_of_items = {"espresso":3.75, "americano":5.65, "latte":4.97}

coins = {
        "penny":0.01,
         "nickle":0.05,
         "dime":0.10,
         "quarter":0.25,
         "half dollar":0.50,
         "dollar coin":1.00
         }


def process_payment(amount:float):
    """will handle change making as well"""
    balance = [] #list of tuples
    sum_of_ballance= 0
    print(f"total: {amount}$\nplease enter the amount of each type of coin used to fufill the ballance")
    # p = input("pennies: ")
    # n = input("nickles: ")
    # d = input("dimes: ")
    # q = input("quarters: ")
    # hd = input("half dollars: ")
    # dc = input("dollar coins: ")
    for i in coins.keys():
        balance.append((i, int(input(f"{i}: "))))
    print(balance)
    for i in range(0, len(balance)):
       sum_of_ballance += coins.get(balance[i][0]) * balance[i][1] # name of coin that refs teh value of the coin * num of coins entered by the user
    print(round(sum_of_ballance,2) )

    if sum_of_ballance < amount:
        return f"insuficent balance, {sum_of_ballance:.2f}"

    elif sum_of_ballance == amount:
        return "suficent balance"
    elif sum_of_ballance > amount:
        # calculate_coin_change()
        change = sum_of_ballance - amount
        return f"suficent balance, your change: {change:.2f}"


def remove_chars_not_in_menu_items(dict_name:dict):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    drinks = list(dict_name.keys())
    drinks_string = "".join(drinks)
    # print(drinks_string)
    letters = []

    # for i in drinks:
    #     letters.append([let for let in i])
    #     # print(letters)

    # successfuly generates my list of letters that are not contained in the menu items!!
    for let in drinks_string:
        if let in alphabet:
            alphabet.remove(let)
    return alphabet

dis_allowed_alphabet = remove_chars_not_in_menu_items(dict_name=recipes)




# has to check if reasorces exist before executing comands

def report_ingredient_status():
    """returns 1 string per ingredient that contains its amount (value) and ingredient name (key)"""
    ingr = ingredeints_in_tank.items() # is a list now
    report_list = [] #stores the report strings

    for i in ingr:
        # print(i) # is a tuple
        # so i can acess it without separating the key val pairs
        #  also this way i can just add items to the dict and thats all i have to do
        name  = i[0]
        amount = i[1]
        report = f'{name}: {amount} {"ml" if name != "coffee" else "g"}'
        report_list.append(report)

    return report_list

    # for i in report_list:
    #     print(i)
#
def resource_check(drink:str): #list of resource amounts
     # why does this work, list wrapped it bc was throwing a instance error
    result_1 ={}
    result = {drink:result_1}

    for n in ingredeints_in_tank:
        if recipes.get(drink).get(n) > ingredeints_in_tank.get(n):
            result_1.update({n: "Insufficient"})
        elif recipes.get(drink).get(n) <= ingredeints_in_tank.get(n):
            result_1.update({n: "Sufficient"})
        else:
            print("look in resouirce check")
    return result


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def make_bevrage(drink:str):
    rc= resource_check(drink).get(drink)


    # ris = report_ingredient_status()

    output = []
    if "Insufficient" in rc.values():
        print(f"sorry insucficent ingredients cannot make {drink}")
    elif "Insufficient" not in rc.values():
        print(process_payment(price_of_items.get(drink)))



def end_sequence():
    return "Thank you for your business"

# print(resource_check("latte"))

while STATE == True:
    user_choice = input("we have available:\nEspresso\nAmericano\nLatte\nWhat beverage would you like today:").strip(" ").lower()
    # s = '@#24l-09=a()&8973t**_##te'
    # user_choice = re.sub(r'[^A-Za-z]', '', s)
    strip_str = ""
    for i in dis_allowed_alphabet:
        strip_str = strip_str.join(i+ " *")



    user_choice = re.sub(r'[^A-Za-z]', '', user_choice) # strips out all non letters
    user_choice = re.sub(f"[{strip_str}]", "", user_choice)

    print(user_choice)
    if user_choice not in recipes.keys():
        print("Sorry invalid input trygain")
    elif user_choice in recipes.keys():
        make_bevrage(user_choice)






    # if user_choice == "exit" or user_choice == "stop" or user_choice == "cancel":
    #     STATE = False
    # elif user_choice == "espresso":
    #     print(make_bevrage("espresso"))
    #     print(end_sequence())
    #
    #
    # elif user_choice == "americano":
    #     print(make_bevrage("americano"))
    #
    # elif user_choice == "latte":
    #     print(make_bevrage("latte"))

# print(make_bevrage("latte"))

# report_ingredient_status()