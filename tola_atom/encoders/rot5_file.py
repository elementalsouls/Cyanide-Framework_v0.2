#!/usr/bin/env python2
def rot5_cipher(message):
	translated = ''
	for character in message:
		if character.isdigit():
			character = (int(character)+5)% 10
		translated = translated + str(character)
	return translated

# Encoding
plaintext = input("Enter the number to be ciphered : ")
ciphertext=rot5_cipher(plaintext)
print("\nYour Ciphered Text is : %s" %ciphertext)

plaintext = ""
plaintext = rot5_cipher(ciphertext) 
