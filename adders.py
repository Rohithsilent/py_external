def half_adder(a,b):
    return a^b,a&b

def full_adder(a,b,carry_in):
    sum1,carry1 = half_adder(a,b)
    sum_result,carry2=half_adder(sum1,carry_in)
    return sum_result,carry1|carry2

def parallel_adder(bits_a,bits_b):
    result=[]
    carry=0
    for a,b in zip(bits_a[::-1],bits_b[::-1]):
        sum,carry=full_adder(a,b,carry)
        result.append(sum)
    if carry:
        result.append(carry)
    return result[::-1]

a = int(input("enter first number:"))
b = int(input("enter second number:"))

print(f"half adder:{half_adder(a,b)}")
print(f"full adder:{full_adder(a,b,1)}")
print(parallel_adder([1,0,1],[1,1,0]))

