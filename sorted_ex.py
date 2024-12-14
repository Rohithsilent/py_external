def sorted_ex(lst):
    sort = sorted(lst)
    if lst == sort:
        return True
    else:
        return False


lst = [1,2,3,4,5]
print(sorted_ex(lst))