import re

USERS = {'user1': '1234', 'user2': '4567'}

def username_check():
	while True:
		user_creation = input('Create your username: ')
		if user_creation in USERS:
			print('cannot be ')
		else:
			print('usr success')
			return user_creation

def password_check():
	while True:
		pwd_creation = input('Type in your password: ')
		if len(pwd_creation) > 7 \
		and re.search("^[a-zA-Z0-9]+", pwd_creation) \
		and re.search("[a-z]+", pwd_creation) \
		and re.search("[A-Z]+", pwd_creation) \
		and re.search("[0-9]+", pwd_creation):
			print('success')
			return pwd_creation
		else:
			print('error')
			

username = username_check()
password = password_check()
USERS[username] = password
print(USERS)

# TODO: improve the print messages
