
s = "Hello world!"
print(s[0])# H
print(s[-1])# !
s = "Hello" 
print(s.upper()) # Виведе 'HELLO'
s = "Some Text"
print(s.lower())  # Виведе 'some text'

num = 15  # приклад значення для num

if num > 10:
    print("num більше за 10")
else:
    print("num не більше за 10")

a = input('Введіть число')
a = int(a)

if a > 0:
    print('Число додатне')
elif a == 1:
    print('Число дорівнює 1')
else:
    print("a <= 0")

a = input('Введіть число')
a = int(a)

if a == 1:
    print('Число дорівнює 1')
elif a > 0:
    print('Число додатне')
else:
    print("a <= 0")