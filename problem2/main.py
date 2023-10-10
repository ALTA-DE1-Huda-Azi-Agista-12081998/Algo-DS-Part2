def maximum_buy_product(money, product_price):
    if money <= 0 or not product_price:
        return 0

    unique_products = set(product_price)
    unique_products_sorted = sorted(unique_products)

    total_price = 0
    count = 0

    for price in unique_products_sorted:
        if total_price + price <= money:
            total_price += price
            count += 1
        else:
            break

    return count

if __name__ == "__main__":
    print(maximum_buy_product(50000, [25000, 25000, 10000, 14000]))      # 3
    print(maximum_buy_product(30000, [15000, 10000, 12000, 5000, 3000])) # 4
    print(maximum_buy_product(10000, [2000, 3000, 1000, 2000, 10000]))   # 4
    print(maximum_buy_product(4000, [7500, 3000, 2500, 2000]))           # 1
    print(maximum_buy_product(0, [10000, 30000]))                        # 0