print("Reverse Number")
print("--------------")
n=int(input("Enter the Number:"))
print("Result")
print("Reverse Number:")
while(n>0):
    r=n%10
    n=n/10
    print(r)
    n=int(n)
