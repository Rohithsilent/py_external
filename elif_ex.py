n = input('enter any thing:')


if n.isdigit():
    print('its a digit')
elif n.islower():
    print('it is a lower case')
elif n.isupper():
    print('it is a upper case')
else:
    print('it is a special character')