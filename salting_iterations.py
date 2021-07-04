import hashlib

data = input("Enter input string: ")

md5 = [];
md5.append(hashlib.md5(b'r2'+data.encode()+b'd2'))
for i in range(1,5):
	md5.append(hashlib.md5(md5[i-1].digest()))

print("Salted and iterated MD5 of provided string is: ", md5[4].hexdigest())