def AND(a,b):
      return a&b
def OR(a,b):
      return a | b
def NOT(a):
      return 1-a
def XOR(a,b):
      return a^b

a = int(input("enter first number:"))       
b = int(input("enter second number:"))
print(f"AND:{AND(a,b)}")
print(f"OR:{OR(a,b)}")
print(f"NOT:{NOT(a)}")
print(f"XOR:{XOR(a,b)}")