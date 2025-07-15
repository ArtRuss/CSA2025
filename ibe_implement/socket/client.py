#client.py
import socket
import json
DISCONNECT_MSG = "!DISCONNECTING"



def main():
    SERVER = socket.gethostbyname(socket.gethostname())
    PORT = 5051
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER, PORT))
    context = get_context() #JSON FORMAT
    call_to_server(s, context)
    response = s.recv(1024).decode('utf-8')
    print(response)
    s.send(DISCONNECT_MSG.encode('utf-8'))

def get_context():
    user_email = input("Enter your email: ")
    try:
        is_sending = int(input("Would you like to send an email? (1 if yes, 0 if no): "))
    except ValueError:
        print("*** Please enter 1 for yes or 0 for no ***")
        get_context()
    if is_sending:
        email_destination = input("Enter the email destination: ")
        message = input("Enter the message to send: ")
    else:
        email_destination = None
        message = None
    context = {
        "identity": user_email, 
        "is_sending": is_sending, 
        "destination": email_destination, 
        "message": message
        }
    return context

def call_to_server(s, context):
    json_context = json.dumps(context)
    s.send(json_context.encode('utf-8'))
    '''
    if context["is_sending"]:
        #Call the encrypt method

    else: #User want's their private key
        #Call the decrypt method
    '''


if __name__ == "__main__":
    main()
