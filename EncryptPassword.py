#Using Vignere Cipher to encrpt password of a user using a key that is private to the user.

def encrypt(password, key):
    n = len(password)

    #Generate key
    if len(key) > n:
        key = key[0:n]
        
    key = list(key) 
    for i in range(n - len(key)): 
        key.append(key[i % len(key)]) 

    key = "" . join(key)

    #Generate encrypted password:
    cipher = []
    for i in range(n):
        letter = (ord(password[i]) + ord(key[i])) % 26
        letter += ord('A')  
        cipher.append(chr(letter))

    print("Encrypted password: " + "".join(cipher))


password = input("Enter password: ")
key = input("Enter your private key: ")
encrypt(password, key)
