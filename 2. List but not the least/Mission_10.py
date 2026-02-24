# https://py.checkio.org/en/mission/stock-profit/

def stock_profit(stock: list[int]) -> int:
    
    buying_point = min(stock)

    if buying_point == stock[-1]:
        stock.pop()

    buying_point = min(stock)

    bp_index = stock.index(buying_point)
    subject_timeline = stock[bp_index:]
    selling_point = max(subject_timeline)


    profit = selling_point - buying_point

    return profit


print("Example:")
print(stock_profit([60, 50, 51, 52, 40]))

# These "asserts" are used for self-checking
assert stock_profit([2, 3, 4, 5]) == 3
assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
assert stock_profit([4, 3, 2, 1]) == 0
assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
assert stock_profit([1, 1, 1, 2, 1, 1, 1]) == 1
assert stock_profit([4, 3, 2, 1, 2, 1, 2, 1]) == 1
assert stock_profit([1, 1, 1, 1]) == 0

print("You are the best broker here! Click 'Check' to earn cool rewards!")
