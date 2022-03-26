import hashlib


def helloUser():
  print("Hello user, this console app is used to encrypt and decrypt your passwords and store them in a seperate text file")

def enterPassword():
  password = input("Enter your password: ")
  return password

    
def encryptor(password):
  encrypted = hashlib.sha256(password.encode()).hexdigest()
  return encrypted

def writeToTextFile(password, encrypted):
  f = open("classified.txt","w+")
  f.write("This is your password: %s\n" % password)
  f.write("This is your encrypted password: %s" % encrypted)
  print("password and encrypted password are saved in a classified file")
  f.close()

# if __name__ == "__main__":
helloUser()
password = enterPassword()
encrypted = encryptor(password)
writeToTextFile(password, encrypted)
