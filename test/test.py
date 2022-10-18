
'''
from re import A


print('Hello World')
# Hello World

print("Python Love Me")
# Python Love Me


print("I'm happy")
# I'm happy

print('He ask me "Who got the Book"')
# He ask me "Who got the Book"


print('\ta\na\ta\ta\n\ta')
#        a
# a      a       a
#        a



print('100.00')
# 100

print('%d' %100)
# 100

print('%d' %100.00)
# 100

print('%f' %100.00)
# 100.000000

print('%.2f' %100.00)
# 100.00



print('My age is',20)
# My age is 20

print('My age is %d I have %.2f Bth.' %(20.0,100.000))
# My age is 20 I have 100.00 Bth.

print('2 + 2 =',2+2)
# 2 + 2 = 4

print('2 + 2 = %.2f' %(2+2))
# 2 + 2 = 4.00

print('2 + 2 = '+ str(2+2))
# 2 + 2 = 4


print('Saharatt',"Pengsuwan")
# Saharatt Pengsuwan

print('Saharatt'+"Pengsuwan")
# SaharattPengsuwan

print('Saharatt '+"Pengsuwan")
# Saharatt Pengsuwan


print(0,1,2,3,4,5,6,7,8,9,)
# 0 1 2 3 4 5 6 7 8 9

print('%d %d %d %d %d %d %d %d %d %d' %(0,1,2,3,4,5,6,7,8,9))
# 0 1 2 3 4 5 6 7 8 9

print('Display the numbers 1 through 5.')
for num in [1,2,3,4,5]:
    print(num)




print('CALCULATING RUNNING TOTAL')
sum = 0 
for num in [1,2,3,4,5]:
    sum += num
    print(sum)

  OUTPUT
CALCULATING RUNNING TOTAL
1 = 0 + 1
3 = 1 + 2
6 = 3 + 3
10 = 6 + 4
15 = 10 + 5


def main():
    for letter in 'Saharatt Pengsuwan':
        if letter == 'a' or letter == 'n':
            continue
        print('Curent Letter :',letter)

def main1():

    for letter in 'Saharatt Pengsuwan':
        if letter == 'a' or letter == 'n':
            break
        print('Curent Letter :',letter)

def main2():

    for letter in 'Saharatt Pengsuwan':
        if letter == 'a' or letter == 'n':
            pass
        print('Curent Letter :',letter)

main2()
'''

'''
โปรแกรมนี้คือโปรแกรม...
1.
2.
'''

def main3():

    score = int(input('Enter score : '))

    while score < 0 or score > 100 : 
        print('ERROR : The score cannot be negative')
        print('or greater than 100.')
        score = int(input('Enter the correct score : '))




def main4():

    keep_going = 'y'

    while keep_going == 'y' :
        name = input('Enter name : ')
        print(name)
        keep_going = input('Enter (y or n) :')

main4()















