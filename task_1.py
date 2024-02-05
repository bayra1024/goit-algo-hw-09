def find_coins_greedy(amount):
    denominations = [50, 20, 10, 5, 2, 1]
    coins_used = {}

    for coin in denominations:
        coins_used[coin] = amount // coin
        amount %= coin

    return coins_used


def find_min_coins(amount):
    denominations = [1, 2, 10, 50]
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    coins_used = {}

    for coin in denominations:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coins_used[i] = coin

    result = {}
    remaining_amount = amount
    while remaining_amount > 0:
        coin = coins_used[remaining_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        remaining_amount -= coin

    return result


# Приклад використання:
amount = 113
print("Greedy Algorithm:", find_coins_greedy(amount))
print("Dynamic Programming:", find_min_coins(amount))
