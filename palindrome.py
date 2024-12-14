def palindrome(s):
    return s ==s[::-1]


s = input("enter a string:")
print(palindrome(s))