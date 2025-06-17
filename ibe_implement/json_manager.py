import json
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
'''
with open("json_ex.json") as file:
    data = json.load(file)
'''
def decrypt_json(key_str, ciphertext_str, nonce_str, tag_str):
    key = base64.b64decode(key_str)
    ciphertext = base64.b64decode(ciphertext_str)
    nonce = base64.b64decode(nonce_str)
    tag = base64.b64decode(tag_str)

    cipher = AES.new(key, AES.MODE_EAX, nonce = nonce)
    #Returns unpadded json string
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    unpadded = unpad(plaintext, AES.block_size)
    decoded = unpadded.decode('utf-8')
    json_contents = json.loads(decoded)
    '''Returns python representation of the json file'''
    return json_contents

    

def get_json_key():
        
    with open("json_ex.json") as file:
        json_str = file.read()

    key = get_random_bytes(16) #Generates a 128 bit key for the AES object

    cipher = AES.new(key, AES.MODE_EAX) #creates AES object needed to perform AES encryption

    ciphertext, tag = cipher.encrypt_and_digest(pad(json_str.encode(), AES.block_size)) #The encrypted version of JSON file
    nonce = cipher.nonce #needed to decrypt
    #Takes byte data and converts it into a string that can act as the message
    key_str = base64.b64encode(key).decode('utf-8')
    ciphertext_str = base64.b64encode(ciphertext).decode('utf-8')
    nonce_str = base64.b64encode(nonce).decode('utf-8')
    tag_str = base64.b64encode(tag).decode('utf-8')
    
    print(f"ciphertext in string form: {ciphertext_str}")
    print(f"key in string form: {key_str}")

    '''key_str is passed as the message to IBE encryption scheme in basicident.py
       The key_str value is a string representation of the bytes of the key used by the cipher object'''
    return key_str, ciphertext_str, nonce_str, tag_str