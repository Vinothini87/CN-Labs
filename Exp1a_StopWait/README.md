# Experiment 1(a) – Stop-and-Wait ARQ

## Aim
To implement the Stop-and-Wait ARQ protocol using Python socket programming.

## Concept
- Layer: Data Link Layer  
- Technique: Flow control & error control  
- Method: Sender sends one frame at a time and waits for acknowledgment.

## Algorithm
1. Start the server and wait for a client.
2. Send one frame and wait for ACK.
3. Upon ACK, send the next frame.
4. Repeat until all frames are transmitted.

## Code
### Server
```python
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
```

## client

```python
import socket
s=socket.socket()
s.connect(('localhost',8080))
while True:
    print(s.recv(1024).decode())
    s.send("Acknowledgement Recived".encode())
```
### Output:
```
C:\vino\19CS406 CN\CN Labs\Exp1a_StopWait>python server.py
Enter a data: hi
Acknowledgement Recived
Enter a data: welcome
Acknowledgement Recived
Enter a data: exit
[SERVER] Closing connection...

C:\vino\19CS406 CN\CN Labs\Exp1a_StopWait>python client.py
hi
welcome
exit
```
### Result

The Stop-and-Wait ARQ protocol was implemented successfully.
The server sends data frames one at a time, and the client acknowledges each frame, ensuring reliable communication.