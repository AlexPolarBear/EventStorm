import socket
                   
HOST = ''                                                                   
PORT = 40005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
    sc.bind((HOST, PORT))
    sc.listen(1)
    connection, address = sc.accept()
    with connection:          
        print('Connected to user_2: %s' % repr(address))                   
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print("Received from user_1: %s" % data)
            data_to_send = input("Enter message to user_2:")
            if not data_to_send:
                break                        
            connection.sendall(bytearray(data_to_send, 'utf-8'))
