
# coding: utf-8




# # Number 1
cm = float(input())
print('Meter: ',cm*0.01,'m')
print('KiloMeter: ',cm*0.00001,'km')


# # Number 2 




c = float(input())
print('Fahrenheit: ',c * 9/5+32,'F')


# # Number 3 




a = int(input())

print(a**a,' ^')


# # Number 4




num = int(input())
if num % 2 == 0:
    print(num,'is even')
else:
    print(num,'is odd')


# # Number 5



char = input()
char.isalpha()


# # Number 6



Num1 = int(input())
Num2 = int(input())
Num3 = int(input())

if Num1 > Num2 and Num1>Num3:
    print('',Num1,'is max numbers')
elif Num2 >Num3:
    print(Num2,'is max numbers')
else :
    print(Num3,'is max numbers')


# # Number 6 using function




Num1 = int(input())
Num2 = int(input())
Num3 = int(input())
number = max(Num1,Num2,Num3)

print(number,'is a max of three numbers')


# # Number 7 




num = input()
l = len(num)
print(l)


# # Number 8




x = 'madam'
x  == x[::-1]


# # Number 9




sen = 'count total number of vowels and consonants in a string'
vowels = list("aeiouy")
consonants = list("bcdfghjklmnpqrstvexz")
v = 0
c = 0
for i in sen:
    
    if i in vowels:
        v+=1
    elif i in consonants:
        c+=1
print('Vowel:',v,'consonants: ',c)


# # Number 10




z = 20


# # Number 11



break = 50 
## break is a keyword . so u can't make it at a variable .for more http://www.pythonforbeginners.com/basics/keywords-in-python/


# # Number 12




1. phone_number = 12345
2. Name = “Benny”



# # Number 15




tup = ('Afridi',2,6.70,False)


# # Number 16 



tup = ('Afridi',2,6.70,False)
li = list(tup)
print(li)


# # Number 17



tup = ['Afridi',2,6.70,False]
del tup[0]
t = tuple(tup)
print(t)


# # Number 18




print(2 + 3 * 4)
# Number 19
a=2
b=3
c=4 
print()
print('result',a+b*c)

## find same result 


# # Number 19




5==5 and 5!=7


# # Number 20 




list1 = ['Afridi',5,7.1,True,'ipy']

list[2] = 5

list2 = ['Rabby',6,False]
l = list + list2
print(l)


# # Number 21




dict = {'Name':'Afridi','email':'afr@gmail.com','post':'1206','hometown':'Comilla','division':'chittagong'}

dict['Name'] = 'Md. Afridi'


dict2 = dict.copy()
print(dict2)
dict.clear()
print(dict)


# # Number 22




num = int(input())
if num < 10:
    print(num,'is less than 10')



# # Number 24




import math
num = int(input())
math.factorial(num)

