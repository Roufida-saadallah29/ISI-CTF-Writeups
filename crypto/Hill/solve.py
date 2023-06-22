import numpy as np

def encrypt(key_matrix, plaintext):
    q = len(plaintext) // 2
    plaintext = [ord(char) - ord('A') for char in plaintext]
    plaintext = np.array(plaintext)
    key_matrix = np.array(key_matrix)
    ciphertext = ""
    for i in range(q):
        chunk = plaintext[i*2 : (i+1)*2]
        chunk_ciphertext = np.dot(key_matrix, chunk) % 26 
        chunk_ciphertext = [chr(char + ord('A')) for char in chunk_ciphertext]  
        ciphertext += ''.join(chunk_ciphertext)

    return ciphertext

# I calculated it with paper
key_inverse = [[13, 17], [11, 19]]
ct = "KCSCCVYGCSBOOVYOTPEIELNSLSGT"
flag = encrypt(key_inverse, ct)
print("flag:", flag)

#PS: M≡(k^-1)C+(−(k^−1)s) I don't know if this is why I didn't get the correct flag

#ISICTFYOUARRTHEKIAGOFTHRHVLL
#ISICTF{YOUARETHEKINGOFTHEHILL}
