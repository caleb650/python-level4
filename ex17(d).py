print("sum of N number")
print("----------------")
a=int(input("Enter the Starting Number:"))
b=int(input("Enter the Ending Number:"))
print("Result")
print("-------")
print("Series")
Count=0
Sum=0
for i in range(a,b+1):
     if(i%5==0)and(i%3==0):
        print("+",+i)
Sum=Sum+i;
Count=+i;
print("Sum Value:",Sum)
print("Count Value:",Count)
    
