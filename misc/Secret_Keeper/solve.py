import string
from pwn import *
from binascii import hexlify, unhexlify




printable = string.printable.replace(" ", "")[:-2]
print(printable)

conn = remote('challenges.isictf.live', 1106)
conn.recvuntil(b"mine: b'")
secretFlag=conn.recvuntil(b"'").decode()
secretFlag = secretFlag[:-1]


secretFlag = unhexlify(secretFlag)  
payload="ISICTF{"
for i in range(7,29):
    for j in range(len(printable)):
        conn.recvuntil(b"quit): ")
        payloadtest=payload+printable[j]
        conn.sendline(payloadtest.encode())

        conn.recvuntil(b"secret: b'")
        flagtest=conn.recvuntil(b"'").decode()
        flagtest = flagtest[:-1]
        flagtest = unhexlify(flagtest) 
        if secretFlag[i]==flagtest[i]:
            print(payloadtest)
            payload=payloadtest
            break
flag=payload+"}"
print(flag)
#ISICTF{1m_n0t_4_s3cr3t_k33p3r}