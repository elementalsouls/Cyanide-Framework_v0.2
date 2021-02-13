import codecs
s = input("Enter a String: ")
ro_encrypt = codecs.encode(s,"rot5")
print("Ciphered Text: ",ro_encrypt)