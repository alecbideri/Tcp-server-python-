import socket 
import threading

# Define the server's IP address and port
target_host = "127.0.0.1"
target_port = 9998

def send_message(client):
    while True:
        # Input message from user
        message = input("Enter a message ('exit' to quit): ")
        
        # Send the message to the server
        client.send(message.encode())
        
        # Check if user wants to exit
        if message.lower() == 'exit':
            break

def receive_messages(client):
    while True:
        try:
            # Receive message from the server
            response = client.recv(1024)
            if not response:
                break
            
            print(f"Server says: {response.decode()}")

        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def main():
    # Create a socket object using IPv4 addressing and TCP protocol
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect the client to the server
        client.connect((target_host, target_port))
        
        # Start a thread to send messages
        send_thread = threading.Thread(target=send_message, args=(client,))
        send_thread.start()

        # Start a thread to receive messages
        receive_thread = threading.Thread(target=receive_messages, args=(client,))
        receive_thread.start()

        # Wait for both threads to finish
        send_thread.join()
        receive_thread.join()

    except Exception as e:
        print(f"Error connecting to server: {e}")

    finally:
        # Close the client socket
        client.close()

if __name__ == '__main__':
    main()
