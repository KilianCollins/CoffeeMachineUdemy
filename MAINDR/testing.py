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
    balance = [] #list of tuples
    sum_of_ballance = 0
    print(f"total: {amount}$\nplease enter the amount of each type of coin used to fufill the ballance")

    for i in coins.keys():
        balance.append((i, int(input(f"{i}: "))))

    print(balance)
    for i in range(0, len(balance)):
        coin,qty = balance[i]
        sum_of_ballance += coins.get(coin) * qty

    print(round(sum_of_ballance,2) )

    if sum_of_ballance < amount:
        return f"insuficent balance, {sum_of_ballance:.2f}"
    elif sum_of_ballance == amount:
        return "suficent balance"
    elif sum_of_ballance > amount:
        change = sum_of_ballance - amount
        return f"suficent balance, your change: {change:.2f}"



print(process_payment(31.90))