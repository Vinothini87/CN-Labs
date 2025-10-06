import socket
s=socket.socket()
s.bind(('localhost',8080))
s.listen(5)
c,addr=s.accept()
while True:
    i=input("Enter a data: ")
    if i.lower() == "exit":       # <-- added exit condition
        c.send(i.encode())        # send 'exit' so client also stops
        print("[SERVER] Closing connection...")
        c.close()
        break
    c.send(i.encode())
    ack=c.recv(1024).decode()
    if ack:
        print(ack)
        continue
    else:
        c.close()
        break