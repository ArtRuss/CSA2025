#client.py
import socket

def main():
    host = "127.0.0.1"
    port = 65432
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(b"Hello world")
    data = s.recv(1024)
    print(f"Recieved data: {data}")


if __name__ == "__main__":
    main()