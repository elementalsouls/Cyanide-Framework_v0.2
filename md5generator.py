import hashlib
plain_txt = input("Please enter the word you want to convert: ")

#Converting your plain text into encoding (utf-8)
text_enc = plain_txt.encode('utf-8')
digest = hashlib.md5(text_enc.strip()).hexdigest()
print("Your generated hash is :" + digest)

