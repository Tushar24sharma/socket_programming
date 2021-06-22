import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#                       ipv4  , UDP type
# Receiver address
recv_addr=("127.0.0.1",9999)
# sending message
user_data=input("Enter your message :- ")
# converting data into ascii code
newdata=user_data.encode('ascii')

s.sendto(newdata, recv_addr)
print("Your message has been sent...")