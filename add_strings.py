def add(filepath):
    words = ["I", "a", ""]
    with open (filepath,'a') as f:
        for word in words:
            f.write('\n'+word)
    
    with open(filepath,'r') as f:
        wordlist =f.read().splitlines()
    return wordlist

        

filepath='words.txt'
print(add(filepath))