import hashlib
flag = 0
pass_hash = input("Please Enter the hash you want to crack :")
pass_file = input("enter the file name :")
try:
    pass_file = open(pass_file, "r")
except:
    print("No file found")
    quit()
for word in pass_file:
    enc_word = word.encode('utf-8')

    digest = hashlib.md5(enc_word.strip()).hexdigest()
    print(word)
    print(digest)
    print(pass_hash)
    if digest == pass_hash:
        print("Password has been found: " + word)
        break

if flag == 1:
    print("Password is not in the list")
