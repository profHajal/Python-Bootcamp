## Print Sum of all Numbers 

## Using Normal form

i = int(input("Enter Number : "))
sum = 0
for i in range(1 , i + 1): 
  
  sum = sum + i
  
print("Result is {0}".format(sum))


## Using Formula 

i = int(input("Enter : "))
sum = 0
for i in range(1 , i+1):
  
  sum = i*(i+1)/2
  
print("Result is {0}".format(round(sum)))