amount = input("Enter the amount:").strip()
coins =[50, 25, 10, 5, 2, 1]
result = {}

def find_coins_greedy(amount: int) -> dict:
    if amount == 0 or amount < 0:
        print("Please anter a valid amount")
        return {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
    return result

def find_min_coins_dynamic(amount: int) -> dict:
    if amount == 0 or amount < 0:
        print("Please anter a valid amount")
        return {}

try:
    amount = int(amount)
    result = find_coins_greedy(amount)
    if result:
        print(result)
except ValueError:
    print("Please anter a valid amount")

