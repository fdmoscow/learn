#numbers = [3, 5, 7, 9 , 10.5]
#print(numbers)

#numbers.append('python')
#print(numbers)
#count_numbers = len(numbers)
#print(count_numbers)

#print(numbers[0])
#print(numbers[-1])
#print(numbers[1:5])
#numbers.remove('python')
#print(numbers)

#DICTIONARIES


#phones = ["Samsung Galaxy S21", "iPhone 12"]

#product = {
    #'name': "iphone XS", 
    #"stock": 5,
    #"price": 300.50,
    #'recommend': phones,
#}

#print(product['recommend'])
#print(product['recommend'][1])

#product['recommend'].append('Iphone6')

#print(product)

stock = [
    {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1, 
       'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
]


print(stock[0])

stock[0]['price'] = stock[0]['price'] + 10000

print(stock[0])

temp_msk = [
    {'city':'Moscow',
     'temp': 20}
]
temp_msk[0]['temp'] = temp_msk[0]['temp'] - 10

print (temp_msk[0].get('country','Russia'))

temp_msk[0]['date'] ="27.05.2019"
print(temp_msk)
print(len(temp_msk))

