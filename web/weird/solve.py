
import requests

url="https://challenges.isictf.live:1418/"


r=requests.post( url ,data={
    "query":"0e215962017"
})

print(r.text)

#ISICTF{php_1s_w31rd_f0r_sur3}

