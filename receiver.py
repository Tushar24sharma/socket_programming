import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#                       ipv4  , UDP type
s.bind(("127.0.0.1",9999))
#creating Udp socket with ipv4 ,port
# code for receive
while True:
    data_recv=s.recvfrom(100)
    print(data_recv)
    #sending reply
    rply="Thanks fr connecting"
    s.sendto(rply.encode('ascii'),data_recv[1])