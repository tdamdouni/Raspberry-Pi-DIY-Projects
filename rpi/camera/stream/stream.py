import socket
import time
import picamera
import datetime as dt

with picamera.PiCamera() as camera:
    #camera.resolution = (800, 600)
    camera.resolution = (1296, 972)
    camera.framerate = 24
    camera.vflip = 1
    camera.annotate_text = 'Office surveillance 3000'
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 4711))
    server_socket.listen(0)
    
    # Accept a single connection and make a file-like object out of it
    connection = server_socket.accept()[0].makefile('wb')
    start = dt.datetime.now()

    try:
        camera.start_recording(connection, format='h264')
        camera.wait_recording(1200)
        camera.stop_recording()
    finally:
        connection.close()
        server_socket.close()
