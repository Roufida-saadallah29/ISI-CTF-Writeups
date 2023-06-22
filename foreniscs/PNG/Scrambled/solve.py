def read_bytes_from_file(file_path):
    with open(file_path, 'rb') as file:
        bytes_data = file.read()
    return bytes_data

# In this challenge i used xxd command to show which parts is the file we have 6 parts

MagicNumber = read_bytes_from_file('X')
IHDR = read_bytes_from_file('N')
IDATX = read_bytes_from_file('Y')
IDAT3 = read_bytes_from_file('3')
IDATC = read_bytes_from_file('C')
IEND = read_bytes_from_file('0')
bytesFIN=MagicNumber+IHDR+IDATX+IDAT3+IDATC+IEND

file_path = 'flag.png'  # Replace with the desired file path

with open(file_path, 'wb') as file:
    file.write(bytesFIN)
