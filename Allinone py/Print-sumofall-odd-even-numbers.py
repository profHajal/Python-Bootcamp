## Print Sum of All Even Numbers

i = int(input("Enter : "))
sum = 0
for i in range(2 , i+1 , 2):
  
  sum = sum + i
  
print("Result is {0}".format(sum))


## Print Sum of All Odd Numbers

i = int(input("Enter : "))
sum = 0
for i in range(1 , i+1 , 2):
  
  sum = sum + i
  
print("Result is {0}".format(sum))