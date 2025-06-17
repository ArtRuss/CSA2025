import json
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
'''
with open("json_ex.json") as file:
    data = json.load(file)
'''
def get_json_key():
        
    with open("json_ex.json") as file:
        json_str = file.read()

    key = get_random_bytes(16) #Generates a 128 bit key for the AES object

    cipher = AES.new(key, AES.MODE_EAX) #creates AES object needed to perform AES encryption

    ciphertext = cipher.encrypt(pad(json_str.encode(), AES.block_size)) #The encrypted version of JSON file
    print(f"ciphertext: {ciphertext}")
    #Takes byte data and converts it into a string that can act as the message
    key_str = base64.b64encode(key).decode('utf-8')
    return key_str

print("\n===========================\n")
print(f"key to pass to basicident.py: {key_str}\n")
'''
for drone in data['drones']:
    print(f"User ID: {drone['identity']}, familiar? {drone['familiar']}")
'''