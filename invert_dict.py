def inverted_dict(d):
    return {value:key for key,value in d.items()}

n = int(input("enter number of elements:"))
user_dict= {}

for _ in range(n):
    key = input("enter key:")
    value =input("enter value:")
    user_dict[key] = value


invertd  = inverted_dict(user_dict)
print(invertd)