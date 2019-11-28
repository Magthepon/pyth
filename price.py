def discounted (price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
      price_for_discount = price
    else:   
      price_for_discount = price - price * discount / 100 
   
    print(price_for_discount)


discounted(10000, 70)