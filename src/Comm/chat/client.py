import socket

HOST = 'localhost'             
PORT = 40005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:                   
    sc.connect((HOST, PORT))
    while True:
        data_to_send = input("Enter message to user_1: ")
        if not data_to_send:
            break
        sc.sendall(bytearray(data_to_send, 'utf-8'))
        data = sc.recv(1024)
        print('Received from user_2: %s'% repr(data))
