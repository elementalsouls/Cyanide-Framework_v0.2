import hashlib
flag = 0
pass_hash = input("Please Enter the hash you want to crack :")
pass_file = input("enter the file name :")
#To open the file into read mode we use- Try and Except
try:
    pass_file = open(pass_file, "r")
except:
    print("No file found")
    quit()
for word in pass_file:
    #when you are to convert any sti=ring in to hash, it requires certain encoding, which is "utf-8" here.
    enc_word = word.encode('utf-8')
    #create a hash digest coz hashing will create a hash object and that also has to be in some hex format.
    #which is called hex digest in technical terms.
    #we are using ".strip()" because of striping of any white spaces it might have.
    digest = hashlib.sha512(enc_word.strip()).hexdigest()
    print(word)
    print(digest)
    print(pass_hash)
    if digest == pass_hash:
        print("Password has been found: " + word)
        break
        #This actually handles if the password is in the list, what if the password is not in the list??
        # To do this we will handle it using flag.


if flag == 1:
    print("Password is not in the list")
