import socket

HEADER=64
port = 5054
FORMAT = 'UTF-8'
disconnect="!We are now disconnect"
server='192.168.1.103'
ADDR=(server,port)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message=msg.encode(FORMAT) #now this is the message that we will send to the server after establishing the connection this encode() function will encode our msg in bytes format for the server which will decode it later
    msg_lenght= len(msg)
    send_lenght= str(msg_lenght).encode(FORMAT) #this send_lenght represents the lenght of the msg that this first msg shouldn't go more than 64 bytes
    send_lenght+= b' ' * (HEADER - len(send_lenght)) #this will add the blank spaces to the messages to match the lenght of the 64 bytes 
    client.send(send_lenght)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))#this is the message from the server side to the client


send("hello world!")
input() #these inputs ar to add space between the messages
send("hello everyone!")
input()
send("hello to the client!")
input()
send(disconnect)
