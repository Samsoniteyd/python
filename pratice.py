# names= ['steph','luuk','tolu','funke', 'biodun', 'kunle', 'fope', 'kemi']

# for name in names:
#     print(name)


# # for na in range(0,14):
# #     print(na)

# for name in range(len(names)):
#     print(names[name])


# def alphabet():
#     word= input('enter any word:')
    
#     vowels = 'a'or 'e'or 'i'or '0'or 'u'
#     if word in vowels:
#         return f'the word you input is vowel'
#     else:
#         return f'the word you input is consonant'
# print(alphabet().lower())
# name='amoo'
# for i in range(6):
#     print(name)


# def sub (num1, num2=4):
#     total= num1 + num2
#     return f'sum is {total}'
# print(sub(6))

# def sumall(num1, num2, num3):
#     total= (num1+num2)-num3
#     total2= num1+num2+num3
#     return f'''
#          sum and sub is {total}
#         sum and sub is {total2}
#     '''
# print(sumall(5,7,9))

# def numg():
#     num = int(input('enter any number:'))
#     if num%2==0:
#         return f'num is even'
#     else:
#         return f'num is odd'
# print(numg())

# word= str(input('enter any letter:'))
# vowel= ('a', 'e', 'i', 'o', 'u')
# if word in vowel:
#     print('it is a vowel')
# elif word.isnumeric():
#     print(f'{word} is not allowed')
# else:
#     print(f'{word} is consonant')

# num1= input('1 enter you number')
# num2= input('2 enter you number:')
# num3= input('3 enter you number')

# if (num1>num2) & (num1>num3):
#     print(f'{num1}is the greatest')
# elif (num2>num1) & (num2>num3):
#     print(f'{num2}is the greatest')
# else:
#     print(f'{num3}is the greatest')

# 
# factorial = 1
# num = int(input('enter any number'))
# for i in range(1, num+1):
#     factorial= factorial*i
#     print(f'the {num} is the {factorial}')

# num = int(input('input any number:'))
# for i in range(1, 13):
#     total = num*i
#     print(f'the {num} * {i}= {total}')
 

# num = int(input('input any number:'))
# for i in range(1, num+1):
#     print('\n')
#     for m in range(1,13):
#         total2 = m*i
#         print(f'{m}* {i}= {total2}')


pwd= 'admine'

for i in range(3):
    chance=2
    password= str(input('enter your password'))
    if (password == pwd):
        print(f'welcome admine')
        break
    else:
        print(f'you have {chance-i} left')
        continue

    