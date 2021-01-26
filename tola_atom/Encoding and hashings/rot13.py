import codecs
s = input("Enter a String: ")
ro_encrypt = codecs.encode(s,"rot13")
print("Ciphered Text: ",ro_encrypt)