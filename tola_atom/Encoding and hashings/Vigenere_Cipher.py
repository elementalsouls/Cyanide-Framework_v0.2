def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))


def cipher_text(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))

string = input("Enter a String: ")
string1 = string.upper()
keyword = input("Enter a key: ")
keyword1 = keyword.upper()
key = generateKey(string1, keyword1)
cipher = cipher_text(string1, key)
print("Cipher Text is: \n"+ cipher)