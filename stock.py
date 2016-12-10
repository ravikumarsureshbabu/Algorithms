#!/usr/bin/python3

stock = input().split()
stock = [ int(x) for x in stock ]

def get_profit(stock):
    sell = -1
    buy = -2
    min_loss = float("-inf")
    max_profit = 0    

    for each in stock:
        profit = buy - sell
        if (profit < 0 ):
            sell = buy = each
            if(profit > min_loss):
                min_loss = profit
        else:
            buy = each
            if profit > max_profit:
                max_profit = profit

    if max_profit == 0:
        return min_loss
    else:
        return max_profit


print(get_profit(stock))
