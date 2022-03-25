import socket 
from threading import Thread


IP , PORT = "127.0.0.1" , 5475
sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
sock.bind((IP,PORT))
sock.listen(2)

client , addr = sock.accept()
print(f"connected to {addr}")
while True :
    cmd = input("Command => ")
    client.send(cmd.encode("utf-8"))
    print(client.recv(102400).decode("utf-8"))
    

    sock.close()