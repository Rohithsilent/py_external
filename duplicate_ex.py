def has_duplicate(lst):
    return len(lst) != len(set(lst))

lst = [1,2,3,4,5,1]
print(has_duplicate(lst))