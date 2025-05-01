import time

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
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    last_coin = [-1] * (amount + 1)
    for coin in coins:
        for current_amount in range(coin, amount + 1):
            if min_coins[current_amount - coin] + 1 < min_coins[current_amount]:
                min_coins[current_amount] = min_coins[current_amount - coin] + 1
                last_coin[current_amount] = coin
    if min_coins[amount] == float('inf'):
        return f"Unable to make {amount} from the given coins."
    result = {}
    while amount > 0:
        coin = last_coin[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    return result

try:
    amount = int(amount)
    start = time.time()
    result_greedy = find_coins_greedy(amount)
    end = time.time()
    
    start = time.time()
    result_dynamic = find_min_coins_dynamic(amount)
    end = time.time()
    
    if result_greedy:
        print(result_greedy)
        print(f"Greedy time: {end - start}")
    if result_dynamic:
        print(result_dynamic)
        print(f"Dynamic time: {end - start}")
except ValueError:
    print("Please anter a valid amount")

