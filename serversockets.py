#simple server socket

import socket

print("Starting socket server")

s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host, port))

s.listen(5)    #blocking, waiting for client connection

while True:
    c, addr = s.accept()   #establish connection with client
    print ("Got connection from addr" + str(addr))
    c.send("Thank you for connecting".encode())
    c.close()      #close connection
    
print("Closing socket server")
    


