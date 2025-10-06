print("sum of n number")
print("________________")
sn=int(input("enter the starting number:"))
en=int(input("enter the ending number:"))
d=int(input("enter the defference:"))
print("result")
print("series")
sum=0
count=0
for i in range (sn,en+1,d):
     print(i,end=" ")
     sum+=i
     count+=1
     print("\sum value:",sum)
     print("\count value:",count)
