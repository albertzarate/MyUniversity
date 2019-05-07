from werkzeug.security import generate_password_hash, check_password_hash

#test below:
hashedword = generate_password_hash('akashisaGOAT')
print hashedword

a = check_password_hash('pbkdf2:sha256:150000$wmARNXGB$13a590f44b6a7997db8ac03a4a71d18c063b614b074d73afbb62ff6381e68a0a', 'akashisaGOAT')
print a

#working example

def showPassWord(key):
	