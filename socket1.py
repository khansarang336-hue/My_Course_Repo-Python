#Connecting web server by using socket and retrieving data from the server
import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #making the socket
mysocket.connect(('data.pr4e.org',80)) #connecting the socket with server
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #creating the variable to send the request to server with UTF-8 encoding
mysocket.send(cmd) #sending the request to server

#collect the reply back with while loop
while True:
    data = mysocket.recv(500) #receiving the data in data variable
    if (len(data)<1):
        break
    print(data.decode()) #printing the data by decoding in unicode
mysocket.close() #closing the connection


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)
mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode())

while True:
    data = mysocket.recv(500)
    if(len(data)<1):
        break
    print(data.decode())
mysock.close()
