import random
import string
chars=" " + string.ascii_letters + string.punctuation + string.digits
chars=list(chars)
key=chars.copy()
random.shuffle(key)
# print(f"chars : {chars}")
# print(f"key : {key}")
#encrypt
plane_text=input("Enter a message to Encrypt : ")
cipher_text=""

for letter in plane_text:
    index=chars.index(letter)
    cipher_text +=key[index]
print(f"original text :{plane_text}")
print(f"Encrypted text :{cipher_text}")
#Decrypt
cipher_text=input("Enter a message to Decrypt : ")
plane_text=""

for letter in cipher_text:
    index=key.index(letter)
    plane_text +=chars[index]
print(f"Encrypted text :{cipher_text}")
print(f"original text :{plane_text}")
