import base64

message = input("Enter a String: ")
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print("Ciphered Text: " + base64_message)