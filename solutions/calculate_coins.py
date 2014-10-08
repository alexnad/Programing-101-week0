coin_values = [100, 50, 20, 10, 5, 2, 1]

def calculate_coins(sum):
    calculated_coins = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0}
    sum *= 100
    
    for value in coin_values:
        while sum >= value:
            print(sum,value)
            sum -= value
            calculated_coins[value] += 1

    return calculated_coins
