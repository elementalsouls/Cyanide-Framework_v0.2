import hashlib

str = input("Enter a String: ")
result = hashlib.md5(str.encode())

print("Hash Equivalent : ", end ="")
print(result.hexdigest())
