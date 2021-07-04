import hashlib

data = input("Enter input string: ")
sha224 = hashlib.sha224(data.encode())
sha512 = hashlib.sha512(data.encode())
blake2s = hashlib.blake2s(data.encode())

print("\nsha224 of provided string is: ", sha224.hexdigest())
print("\nsha512 of provided string is: ", sha512.hexdigest())
print("\nblake2s of provided string is: ", blake2s.hexdigest())