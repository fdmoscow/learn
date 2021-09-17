a = "Python"
b = "world"
c = "2"
d = f'{a} {b} {c}'

print(d.upper())
print(len(d))

user_hi = " Привет   "
print(user_hi.strip())

example1 = " ПриветЫ ".lower().replace('ы', ' ').capitalize().strip()
print(example1)

exapmle2 = "Предложение из нескольких слов"
print(len(exapmle2.split()))

x = None
y = 0
print (x is None)
print (y is None)

age = int(input('How old are you? - '))
age = 2021 - age
print (f'You were born in {age}!')

