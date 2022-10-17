def encrypt(message, key):
    cipher = ""
    for i in message:
        if i.isupper():
            cipher += chr((ord(i) + key - 65) % 26 + 65)
        elif i.islower():
            cipher += chr((ord(i) + key - 97) % 26 + 97)
        else:
            cipher+=" "

    return cipher

message = input("Enter the message:")
print("Cipher:", encrypt(message, 3))

# Decryption part
def decrypt(cipher, key):
    message = ""
    for i in cipher:
        if i.isupper():
            message += chr((ord(i) - key - 65) % 26 + 65)
        elif i.islower():
            message += chr((ord(i) - key - 97) % 26 + 97)
        else:
            message+=" "
    return message

cipher = input("Enter the cipher:")
print("Message: ", decrypt(cipher, 3))
