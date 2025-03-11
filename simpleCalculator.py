
print('+')
print('-')
print('*')
print('/')

x = input('choose an operation: ')
if x in ['+', '-', '*', '/']:
  num1 = int(input('type a number: '))
  num2 = int(input('type a number: '))
if (x == ('+')):
  print(num1 + num2)
elif (x == ('-')):
  print(num1 - num2)
elif (x == ('*')):
  print(num1 * num2)
elif (x == ('/')):
  print(num1 / num2)
else:
  print("invalid entry")

    
     