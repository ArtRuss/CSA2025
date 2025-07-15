#server.py
import socket

#def is_port_open():

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 65432
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Address: {addr}")
        while True:
            data = conn.recv(1024)
            '''if data:
                conn.sendall(data)
            else:
                break'''
            if data == b'':
                break
            else:
                conn.sendall(b"Your message was recieved")
            print(f"Received {data}")


if __name__ == "__main__":
    main()