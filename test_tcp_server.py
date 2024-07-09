import socket 
import threading

# Define the server's IP address and port
IP = '0.0.0.0'
port = 9998

# List to store all connected client sockets
clients = []

def main():
    # Create a TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the server to the specified IP address and port
    server.bind((IP, port))
    # Listen for incoming connections with a backlog of 5
    server.listen(5)
    print(f"[*] Listening on {IP}:{port}")

    while True:
        # Accept a client connection
        client, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")
        
        # Add the client socket to the list
        clients.append(client)

        # Start a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    try:
        while True:
            # Receive data from the client
            request = client_socket.recv(1024)
            if not request:
                break

            # Broadcast the message to all connected clients
            broadcast_message(client_socket, request)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Remove the client socket from the list
        clients.remove(client_socket)
        # Close the client socket
        client_socket.close()

def broadcast_message(sender_socket, message):
    # Iterate through all connected clients
    for client in clients:
        # Send the message to every client except the sender
        if client != sender_socket:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error broadcasting message: {e}")

if __name__ == '__main__':
    main()
