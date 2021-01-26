import hashlib
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha512(hash_string.encode()).hexdigest()
    return sha_signature
hash_string = input("Enter a String: ")
sha_signature = encrypt_string(hash_string)
print("Hash Equivalent : ", end ="")
print(sha_signature)