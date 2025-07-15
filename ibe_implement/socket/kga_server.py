#kga_server.py
import socket
import threading
import logging
import json
import basicident
DISCONNECT_MSG = "!DISCONNECTING"

class Client:
    def __init__(self, client_number, user_email=""):
        self.user_email = user_email
        self.is_sending = 0
        self.message = ""
        self.client_number = client_number
    
    def set_user_email(self, email):
        self.user_email = email
    
    def set_message(self, message):
        self.message = message
        self.is_sending = 1


def start(s, SERVER, ibe, E):
    s.listen()
    #print(f"[LISTENING] on server {SERVER}")
    logger.info(f"[LISTENING] on server {SERVER}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, ibe, E))
        thread.start()
        #print(f"[ACTIVE CLIENTS] {threading.active_count() - 1}")
        logger.info(f"[ACTIVE CLIENTS] {threading.active_count() - 1}")

def handle_client(conn, addr, ibe, E):
    #print(f"[NEW CONNECTION] {addr} connected")
    logger.info(f"[NEW CONNECTION] {addr} connected")
    client_number = threading.active_count() - 1
    current_client = client_list[client_number]
    '''user_email = input("Enter your email: ")
    current_client.set_user_email(user_email)
    is_sending = int(input("1 to send an email"))
    if is_sending:
        email_destination = input("Enter the email destination: ")
        message = input("Enter the message to send: ")
        current_client.set_message(message)
    '''
    while True:
        json_context = conn.recv(1024).decode('utf-8')
        if json_context == DISCONNECT_MSG:
            break
        context = json.loads(json_context) #JSON file
        print("\nDetails of connecting user\n---------------")
        for key, value in context.items():
            print(f"{key}: {value}")
        print("---------------")
        #print(f"[MESSAGE RECEIVED] {message}")
        logger.info(f"[CONTEXT RECEIVED] {context}")
        conn.send("Message recieved".encode('utf-8'))
        client_data = basicident.handle_context(context, ibe, E)
        for key, value in client_data.items():
            print(f"{key}: {value}")
    conn.close()

#def context_manager(context):
    
def main(ibe, E):
    global client_list
    client_list = [Client(i) for i in range(10)]

    global logger 
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='server.log', level = logging.INFO, encoding='utf-8', filemode='w')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER = socket.gethostbyname(socket.gethostname())
    port = 5051
    s.bind((SERVER, port))
    start(s, SERVER, ibe, E)

if __name__ == "__main__":
    main()