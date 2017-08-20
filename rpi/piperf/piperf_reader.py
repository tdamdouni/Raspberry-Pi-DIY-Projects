## Server (wearing a unicornhat)
import piperf
import socket

HOST = ''
PORT = 55555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print "Connected by", addr
while 1:
    data = conn.recv(1024)
    values = [float(x) for x in data.split("\t")]
    print data
    piperf.monitor_pi(values[0], values[1], values[2], values[3])
    piperf.clean()
    if not data: break
#conn.sendall(data)
conn.close()
