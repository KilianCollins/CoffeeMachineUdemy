# price_of_items = {"espresso":3.75, "americano":5.65, "latte":4.97}
#
# coins = {
#         "penny":0.01,
#          "nickle":0.05,
#          "dime":0.10,
#          "quarter":0.25,
#          "half dollar":0.50,
#          "dollar coin":1.00
#          }
#
#
#
# def process_payment(amount:float):
#     balance = [] #list of tuples
#     sum_of_ballance = 0
#     print(f"total: {amount}$\nplease enter the amount of each type of coin used to fufill the ballance")
#
#     for i in coins.keys():
#         balance.append((i, int(input(f"{i}: "))))
#
#     print(balance)
#     for i in range(0, len(balance)):
#         coin,qty = balance[i]
#         sum_of_ballance += coins.get(coin) * qty
#
#     print(round(sum_of_ballance,2) )
#
#     if sum_of_ballance < amount:
#         return f"insuficent balance, {sum_of_ballance:.2f}"
#     elif sum_of_ballance == amount:
#         return "suficent balance"
#     elif sum_of_ballance > amount:
#         change = sum_of_ballance - amount
#         return f"suficent balance, your change: {change:.2f}"
#
#
#
# print(process_payment(31.90))

recipes = {
    "espresso": {"water": 50, "milk": 0, "coffee": 50},
    "americano": {"water": 100, "milk": 0, "coffee": 50},
    "latte": {"water": 50, "milk": 100, "coffee": 50}
}

price_of_items = {"espresso":3.75, "americano":5.65, "latte":4.97}
# alphabet = list(map(chr, range(97, 123)))


#
# def remove_chars_not_in_menu_items(ui:str = ""):
#     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#     dis_allowed_alphabet = []
#
#
#     drinks = list(recipes.keys())
#     drinks_string = "".join(drinks)
#     # print(drinks_string)
#     letters = []
#
#     # for i in drinks:
#     #     letters.append([let for let in i])
#     #     # print(letters)
#
#     # successfuly generates my list of letters that are not contained in the menu items!!
#     for let in drinks_string:
#         if let in alphabet:
#             alphabet.remove(let)
#     print(alphabet)
#
# remove_chars_not_in_menu_items()



# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# dis_allowed_alphabet = []
#
#
# drinks = list(recipes.keys())
# drinks_string = "".join(drinks)
# # print(drinks_string)
# letters = []
#
# # for i in drinks:
# #     letters.append([let for let in i])
# #     # print(letters)
#
# # successfuly generates my list of letters that are not contained in the menu items!!
# for let in drinks_string:
#     if let in alphabet:
#         alphabet.remove(let)
# print(alphabet)
#


def remove_chars_not_in_menu_items(ui: str = ""):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    drinks = list(recipes.keys())
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

dis_allowed_alphabeta = remove_chars_not_in_menu_items()




