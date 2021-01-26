import base64

string = input("Enter a String: ")
string_byte = string.encode("ascii")
base64_bytes = base64.b64encode(string_byte)
base64_string = base64_bytes.decode("ascii")
print("Encoded String:  " + base64_string)
