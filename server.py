import socket
import threading

HEADER = 64 #since we don't know the actual lenght of the msg that we're going to receive from the client
port = 5050

server = socket.gethostbyname(socket.gethostname()) #this gives our local pc ip address
ADDR=(server,port)
FORMAT= 'utf-8'
DISCONNECT= "!We are now disconnect"
server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)# (socket.SOCK_STREAM) this is defining that we are streaming our data to the socket
# (socket.AF_INET) stands for the type of ip address Af_INET6 stands for iPV6 , it specifies the type of addresses that we're working for
server.bind(ADDR)

def client_handling(connect,ADDR):#this will handle the individual connection
    print(f"[NEW CONNECTIONS]{ADDR} connected.")
    connected=True
    while connected:
        msg_lenght = connect.recv(HEADER).decode(FORMAT)#first is to know the lenght of the msg that we are about to receive
        if msg_lenght!= None:
            msg_lenght = int(msg_lenght) # we use that and convert msg into the integer
            msg = connect.recv(msg_lenght).decode(FORMAT)#how many bytes we're gonna be receiving for the actual msg

            if msg == DISCONNECT:#this disconnection is because if the client is partially disconnected from their side but for our server they will be represented as connected
                                 #to overcome this issue as the client is disconnect the server will set them the msg typed in the disconect
                connected=False

            print(f"[{ADDR}] {msg}")#printing out the address of the client and the msg whatever they have sent
    connect.close()

def start():#where as this function will handle all the new clients infinite times

    server.listen()
    print(f"[LISTENING] server is listening at...{server}")
    while True:
        connect,ADDR=server.accept()#this connect this basically passing the connection or allwing su to communicate back with the client or the thing that is connected with the server
        #addr is the info about the client

        thread= threading.Thread(target=client_handling,args=(connect,ADDR))
        thread.start()#thid thread will track the no of connections made but since the one start() thread was continously active so the actual number of thread would be one less then the number of threads
        print(f'[ACTIVE CONNECtIONS]{threading.active_count()-1}')


print("[STARTING]server is starting...")
start()
