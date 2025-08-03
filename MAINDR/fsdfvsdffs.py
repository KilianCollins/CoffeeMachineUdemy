from typing import AnyStr

# coffe machine
# 7-25-25

STATE = True
ingredeints_in_tank = {"water":10000, "milk":1, "coffe":100000}

# i did it like this bc i wanted a way to ref the menu item and have its reqs right there i also wanted them to be less memoru intesne so i made them immutable

# oh boy

recipes = {
           "espresso":[
                       ("water",50),
                       ("milk",0),
                       ("coffe",50)
                      ],

           "americano":[
                       ("water",100),
                       ("milk",0),
                       ("coffe",50)
                      ],

           "latte":[
                       ("water",50),
                       ("milk",100),
                       ("coffe",50)
                      ]
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



#
# def state_manager(inputU:str):
#     inputU = inputU.lower().strip(" ")
#     if inputU == "off":
#         return False
#     else:
#         return True

# def off():





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
        report = f'{name}: {amount} {"ml" if name != "coffe" else "g"}'
        report_list.append(report)

    return report_list

    # for i in report_list:
    #     print(i)
#
def resource_check(drink:str): #list of resource amounts
    ingr = list(ingredeints_in_tank.items()) # why does this work, list wrapped it bc was throwing a instance error
    result = []

    for n in range(0, len(ingredeints_in_tank)):
        # oh man what have i done
        #  should be the equivalent values
        if ingr[n][1] < recipes.get(drink)[n][1]:
            # print(f"not enough {ingr[n][0]}, cannot make {drink}")
            result.append((ingr[n][0],"insuficient"))


        elif ingr[n][1] >= recipes.get(drink)[n][1]:
            result.append((ingr[n][0],"suficient"))

    return result

        # print(recipes.get(drink)[n][1])

# print(len(ingredeints_in_tank.values()))

# print(ingredeints_in_tank.get(ingredeints_in_tank[1]))

# print(ingredeints_in_tank[0])

# def payment_check(payment)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def make_bevrage(drink:str):
    # diplay "payment toatl and "payment sucesssful"
    # display "here is you change"
    rc= resource_check(drink)
    ris = report_ingredient_status()

    output = []

    r = []
    for i in rc:
        r.append(i[1])
    if "insuficient" in r:
        print("FALSE",f"Sorry insuficent ingredents for {drink} please buy something else your payment was refunded")

    elif "insuficient" not in r:
        print("TRUE",f"Here is your {drink}")

    return r



    # return output

def end_sequence():
    return "Thank you for your business"

# print(resource_check("latte"))

while STATE == True:
    user_choice = input("we have available:\nEspresso\nAmericano\nLatte\nWhat beverage would you like today:").strip(" ").lower()
    bev = list( make_bevrage(user_choice))
    print(process_payment(price_of_items.get(user_choice)))

    for i in range(0,len(bev)):
        if user_choice in recipes.keys():
            if "FALSE" in bev[i]:
                print("sorry")
            elif "TRUE" in bev[i]:
                print(bev[i])




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