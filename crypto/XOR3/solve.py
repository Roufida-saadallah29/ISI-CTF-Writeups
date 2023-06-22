from pwn import xor

ct = '4953491504467d2865765b7d2f614f640f0d7d0e5f67212b2d292f28786671746027191a54446a0c4b023e503a6c076a3e5e5012455016497866712230271f4b01476e4516502e006a394a363e54454a1c4a4b1c'
ct = bytes.fromhex(ct)

k1 = b'****************************'
k2 = b'****************************'

a = ct[:len(k1)]
b = ct[len(k1):len(k1)+len(k2)]
c = ct[len(k1)+len(k2):]

flag = xor(xor(a, b, k2), c, k1)

print(flag.decode())
