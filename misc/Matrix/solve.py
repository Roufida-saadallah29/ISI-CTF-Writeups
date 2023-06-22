from pwn import *


def find_indices(matrix):
    indices = []
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 1:
                indices.append(f'{i+1}{chr(j+97)}')
    return indices

conn = remote('challenges.isictf.live', 1102)
conn.recvuntil(b"good luck :)\n\n\n")

for t in range(100):
    data=conn.recvuntil(b"\n\n")
    lines = data.decode().split('\n')
    lines = [line for line in lines if line.strip()]
    values = [line.split('\t')[1:] for line in lines[1:]]
    matrix = [[int(value) for value in row] for row in values]
    indices = find_indices(matrix)
    conn.recvuntil(b"your answer: ")
    indices = ','.join(indices).encode()
    conn.sendline(indices)
    conn.recvuntil(b"\n")
conn.recvline()
print(conn.recvline())

conn.close()

#ISICTF{my_f1r57_pr0gr4m1ng_ch4ll_y4y}