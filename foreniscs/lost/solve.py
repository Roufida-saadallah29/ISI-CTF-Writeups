def read_bytes_from_file(file_path):
    with open(file_path, 'rb') as file:
        bytes_data = file.read()
    return bytes_data

data = read_bytes_from_file('flag.broken')
data = b"\xfd7zX"+data

#To decompress it, use :xz -d -v flagxz.xz
#and then unzip it 
f=open('flagxz.xz', 'wb')
f.write(data)

# flag : ISICTF{Y0U_r3cOvEr3D_7H3_fILE_4lL_7hAnkS_to_hfz} 
