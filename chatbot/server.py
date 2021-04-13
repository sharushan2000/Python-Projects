import socket
#

class Server :
    def __init__(self):
        self.user = input("Enter Your Name :")
        self.server_ip = "192.168.43.254"
        self.port = 4444
        self.s = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
        self.s.bind((self.server_ip,self.port))


    def connecting(self):
        print("Waiting for connection ")
        self.s.listen()
        self.conn, self.addr = self.s.accept()
        print(self.addr[0] , "connected")
        

    def ackno(self):
        self.connecting()
        self.conn.send(self.user.encode())
        self.patner = self.conn.recv(1024).decode()
        print("connnected with " ,self.patner)
       
    
    def communication(self):
        self.ackno()
        while True :
            send_msg = input(self.user + "      -->")
            self.conn.send(send_msg.encode())
            if send_msg == "bye":
                self.conn.close()
                break

            recv_msg = self.conn.recv(1024).decode()
            print(self.patner +"  -->" + recv_msg)
            if recv_msg == "bye":
                self.conn.close()
                break
            



        




if __name__ == "__main__":
    s =Server()
    s.communication()
    





