import socket

class Client:
    def __init__(self):
        self.user = input("Enter Your Name :")
        self.ip = "192.168.43.254"
        self.port = 4444
        self.c = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
        

    def connecting(self):
        self.c.connect((self.ip,self.port))

    def ackno(self):
        self.connecting()
        self.patner = self.c.recv(1024).decode()
        print("connected with" ,self.patner)
        self.c.send(self.user.encode())
       
    def communication(self):
        self.ackno()
        while True:
            recv_msg = self.c.recv(1024).decode()
            print(self.patner + "  -->" ,recv_msg )
            if recv_msg == "bye":
                self.c.close()
                break
            send_msg = input(self.user + "     -->")
            self.c.send(send_msg.encode())
            if send_msg == "bye":
                self.c.close()
                break
                
            





if __name__ == "__main__":
    c = Client()
    c.communication()