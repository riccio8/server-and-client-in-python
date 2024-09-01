import socket
import time


HOST = socket.gethostbyname(socket.gethostname())
print(HOST)
PORT = 9091



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


server.listen()


while True:
    communication_socket, address = server.accept()
    print(f"Si è collegato l'utente {address}")
    if (communication_socket != None):
        while True:
            message = communication_socket.recv(2048).decode("utf-8")
            print("Il meessaggio dall'utente è: " + (message).decode)
            communication_socket.send(f"Ho ricevuto il tuo messaggio!! Grassie".encode("utf-8"))
    time.sleep(60)
    communication_socket.close()
    print(f"La comunicazione con l'utente {address} è terminata")
    # questo è il server tcp
