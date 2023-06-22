import os
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from pwn import *



con= remote("challenges.isictf.live", 1300)
con.recvuntil(b"> ")
con.sendline(b"2")
con.recvuntil(b"name: ")
con.sendline(("A"*AES.block_size+"adel").encode())
token=con.recvline().decode().split(":")[1].strip()[32:]
con.recvuntil(b"> ")
con.sendline(b"1")
con.sendline(token.encode())
print(con.recvline())

#ISICTF{i_br0k3_y0ur_p4dd1ng_4nd_y0ur_h34rt}