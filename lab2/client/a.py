import socket

DEST_IP = '192.168.183.195'
DEST_PORT = 50000
ENCODER = "utf-8"
BYTESIZE = 1024

# Create a client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))
#It creates a new socket (client_socket) using IPv4 (socket.AF_INET) and
# TCP (socket.SOCK_STREAM). It then connects to the server using the specified IP address and port.

while True:
    # Receive information from the server
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    # Quit if the connected server wants to quit, else keep sending messages
    if message.lower() == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat... goodbye!")
        break
    else:
        print(f"\n{message}")
        user_input = input("Message: ")
        client_socket.send(user_input.encode(ENCODER))

client_socket.close()


# Message: Hello


#Message: CAPITALIZE Make it


#Message: CHECK 23 prime


#Message: CHECK 121 palindrome


#Message: quit
