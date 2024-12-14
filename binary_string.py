def binary(n,binary_string=''):
    if n==0:
        print(binary_string)
    else:
        binary(n-1,binary_string+'0')
        binary(n-1,binary_string+'1')

n = int(input("enter number:"))
binary(n)
