def capitalise(sentence):
    result = ''
    words = sentence.split()
    for word in words:
        new_word = word[0].upper()+word[1:]
        result += new_word + ' '
    return result.strip()

sentence = input("enter a sentence:")
capital = capitalise(sentence)
print(capital)
