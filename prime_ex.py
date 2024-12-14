start = int(input("enter starting number:"))
end = int(input("enter ending number:"))

for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num % i == 0:
                done = False
                break
        else:
            print(num)
