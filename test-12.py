import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
port = 9999
s.bind((host,port))

while True:
    data,addr=s.recvfrom(1024)
    print('from:'+str(addr))
    print('text:'+str(data.decode('utf-8')))
    s.sendto(data.decode('utf-8').upper().encode(),addr)








