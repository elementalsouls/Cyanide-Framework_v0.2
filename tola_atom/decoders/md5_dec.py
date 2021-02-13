import hashlib

count = 1

md5_pass = input("Enter the Hash Text: ")
md5_file = input("Do you need to give a Custom Dictionary(Y/N): ")
if (x == "Y") or (x == "Yes") or (x == "YES"):
    md5_file = input("Enter Wordlist Location: ")
elif (x == "N") or (x == "No") or (x == "NO"):
    md5_file = "/usr/share/wordlists/rockyou.txt"



    for password in md5_file:
        hash = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
        print("[*] Trying Password %d ===> %s" % (count,password.strip()))
        count += 1

        if hash == y:
            print("Password Found, Password is: %s" % passwords)
            break
# else:
#     print("Password Not Found")
