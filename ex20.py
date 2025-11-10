print("Prime Number Checking")
print("---------------------")
n=int(input("Enter the number:"))
print("Result")
count=0
for i in range(2,n):
  if(n%i==0):
      count=1
  if count==0:
      print(n,"is a prime")
  else:
     print(n,"is a not prime")
