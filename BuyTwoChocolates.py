#https://leetcode.com/problems/buy-two-chocolates/
def buyChoco(self, prices, money):
    chocoload_1 = min(prices)
    prices.remove(min(prices))
    pay = min(prices) + chocoload_1
    if pay > money:
        return money
    else:
        return money - pay
prices = [3,2,3]
money = 3
print(buyChoco(prices,money))
