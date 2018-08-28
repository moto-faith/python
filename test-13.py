import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
port = 9999
addr=('{}'.format(host),port)
while True:
    data = input('请输入:')
    s.sendto(data.encode('utf-8'),addr)
    recvdata,addr=s.recvfrom(1024)
    print(recvdata.decode('utf-8'))
s.close()



