#def discounted (price, discount, max_discount = 100):
    #price = abs(float(price))
    #discount = abs(float(discount))
    #max_discount = abs(float(max_discount))
    #if max_discount > 99:
     #   raise ValueError ('Макс скидка не может быть больше 99%')
    #if discount>=max_discount:
     #   price_with_discout = price
    #else:
     #   price_with_discout = price - price*discount/100
    #return (price_with_discout)
    
#product = {'name': 'Samsung Galaxy S21', 'price': 50000.0,  'discount': 49}
#product['with_discount'] = discounted(product['price'], product['discount'])

#print(product)

def get_summ(one, two, delimiter='&'):
        one = str(one)
        two = str(two)
        get_result = (one + delimiter +  two)
        print(get_result.upper())
        

get_summ('learn', 'python')

def format_price(price):
    price = int(price)
    return(f"Цена: {price} руб.")
res = format_price(56)
print(res)








