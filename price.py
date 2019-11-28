def discounted (price, discount, max_discont = 70):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= max_discont:
      price_for_discount = price
    else:   
      price_for_discount = price - price * discount / 100 
   
    print(price_for_discount)


discounted(10000, 37)