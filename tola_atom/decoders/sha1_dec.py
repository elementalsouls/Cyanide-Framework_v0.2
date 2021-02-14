import hashlib
flag = 0
pass_hash = input("Please Enter the hash you want to crack :")
optn = input("Do you want to Give a Custom Dictionary(Y/n)")
if (optn=="Y") or (optn=="y") or (optn=="yes"):
    pass_file = input("enter the file name :")
    try:
        pass_file = open(pass_file, "r")
    except:
        print("No file found")
        quit()
    for word in pass_file:
        enc_word = word.encode('utf-8')

        digest = hashlib.sha1(enc_word.strip()).hexdigest()
        print(word)
        print(digest)
        print(pass_hash)
        if digest == pass_hash:
            print("Password has been found: " + word)
            break
elif (optn=="N") or (optn=="n") or (optn=="no"):
    pass_file = "/usr/share/wordlists/rockyou.txt"
    try:
        pass_file = open(pass_file, "r")
    except:
        print("No file found")
        quit()
    for word in pass_file:
        enc_word = word.encode('utf-8')

        digest = hashlib.sha1(enc_word.strip()).hexdigest()
        print(word)
        print(digest)
        print(pass_hash)
        if digest == pass_hash:
            print("Password has been found: " + word)
            break

if flag == 1:
    print("Password is not in the list")
