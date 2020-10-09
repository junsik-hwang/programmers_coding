# leetcode 121. Best Tiem to Buy and Sell Stock

prices = [7,1,5,3,6,4]

min_price = max(prices)
profit = 0

for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)

print(profit)