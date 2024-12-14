def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

a = int(input("enter first number:"))       
b = int(input("enter second number:"))
print(gcd(a,b))