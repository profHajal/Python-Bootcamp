count = 0
count2 = 0

num = int(input("How Many ?"))

for i in range(0,num):
  
  n = int(input())
 
  if n > 0 :
    count += 1
    
  else:
    count2 +=1

print("{0} Positive Number/s".format(count))
print("{0} Negetive Number/s".format(count2))