import hashlib
message = "Some text to hash".encode()
print("SHA-256:", hashlib.sha256(message).hexdigest())