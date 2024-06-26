import socket 
import threading

IP = '0.0.0.0'
port = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, port))
    server.listen(5)
    print(f"[*] Listening on {IP}:{port}")

    while True:
        client, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f'[*] Received: {request.decode("utf-8")}')
    # Send a different acknowledgment message
    client_socket.send(b"Hello from the server!")  # Changed message
     # Close the client socket after sending the response

if __name__ == '__main__':
    main()
