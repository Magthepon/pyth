def discounted (price, discount):
    if discount >= 100:
      price_for_discount = price
    else:   
      price_for_discount = price - price * discount / 100 
   
    print(price_for_discount)


discounted(1050, 20)