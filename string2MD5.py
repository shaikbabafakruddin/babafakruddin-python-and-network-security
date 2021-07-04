import hashlib

data = input("Enter input string: ")
md5 = hashlib.md5(data.encode())

print("MD5 of provided string is: ", md5.hexdigest())