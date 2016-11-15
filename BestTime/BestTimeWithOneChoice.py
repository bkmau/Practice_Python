list = [3, 2, 6, 5, 6, 1, 2, 6, 1]
list2 = [x - max(list) for x in list]
profit = 0
day_to_buy = 0
day_to_sell = 0

for i, j in enumerate(list2):
    if j == 0:
        if i > day_to_sell:
            day_to_sell = i
if day_to_sell != 0:
    profit = abs(min(list2[0:day_to_sell]))
    day_to_buy = list2.index(min(list2[0:day_to_sell])) + 1

if profit == 0:
    print("Can't get any profit in this investment")
else:
    print("To earn the best profit, {}, of stock, as buy at day {} and sell at day {}".format(
        profit, day_to_buy, (day_to_sell + 1)
    ))
