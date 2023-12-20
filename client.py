import socket


HOST = '' # write here the ipv4 address of the server
PORT = 9091



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
while True:
    message = input("scrivi un messaggio: ")
    message = codifica(message)
    mess = client.sendto(message.encode(), (HOST, PORT))
    # client tcp
