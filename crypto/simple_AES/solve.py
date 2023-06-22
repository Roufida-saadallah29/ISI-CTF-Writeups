from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import hexlify, unhexlify
from Crypto.Util.Padding import pad
            
        
iv = "813c5def8998acecf96ae0fd8c0af844"
ct = "8ceeab5f2db4424386053833f2bd9144f6d52e23f1c2cb30ca4e6895b9a7f9e5"

iv=unhexlify(iv)
ct=unhexlify(ct)
for i in range(256):  
    for j in range(256):
        payload=pad(i.to_bytes()+j.to_bytes(), 16)  
        cbc = AES.new(payload, AES.MODE_CBC, iv)
        flag = cbc.decrypt(ct)
        if b"ISICTF{" in flag:
            print(flag)
            break
