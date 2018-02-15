
# coding: utf-8

# # Number 23 

# In[ ]:


n = int(input())
if n % 2==0:
    print('Even')
else:
    print('Odd')
    
n = int(input())    
if n % 10 ==0 or n % 50 ==0 :
  
  if n % 30 == 0: 
        
      print("Divisible by 10,50,30")
  else:
    print("This number divisible by 10 and 50 but not 30")
    


# # Number 27

# In[ ]:


n = int(input())
for row in range(1,n+1):
    print('*',end='')


# # Number 28

# In[ ]:


r = int(input())
c = int(input())
for row in range(1,r+1):
    for column in range(1,c+1):
        print('*',end = '')
    print()    
    


# # Number 29

# In[ ]:


n = int(input())
for row in range(1,n+1):
    for column in range(1,row+1):
        print('*',end = '')
    print()    


# # Number 30

# In[ ]:


n = int(input())
for i in range(0, 5):
    for j in range(0, n+2):
        print(end=" ")
    n = n - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()


# # Number 31

# In[ ]:


n = int(input())
for i in range(0, n):
    for j in range(0, n):
        print(end=" ")
    n = n - 1
    for j in range(0, i+1):
        print("* ", end="")
    print()


# # Number 32

