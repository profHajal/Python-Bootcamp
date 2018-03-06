## Day 0 : Hello, World.

input_string = input()

print('Hello, World.')
print(input_string)


## Day 1 : Data Types

i2 = int(input())
d2 = float(input())
s2 = input()

print(i+i2)
print(d+d2)
print(s+s2)

## Day 2 : Operators

total = 0
meal = float(input())
tip = int(input())
tax = int(input())
t = meal * tip / 100
r = meal * tax / 100
total = meal + t + r

print("The total meal cost is {0} dollars.".format(round(total)))


## Day 3 : Intro to Conditional Statements

n = int(input())
if n% 2 != 0:
    print("Weird")
elif n % 2 == 0 and n in range(2,6):
    print("Not Weird")
elif n % 2 == 0 and n in range(6,21):
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
    
    
## Day 5 : Loops

n = int(input())
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    
    
## Day 6 : Let's Review

for N in range(int(input())):
    S = input()
    print(S[::2], S[1::2])