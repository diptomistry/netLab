
import socket
import math

HOST_IP = '192.168.183.195'
HOST_PORT = 50000
ENCODER = "utf-8"
BYTESIZE = 1024


def capitalize_text(text):
    return text.upper()

def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def check_palindrome(string):
    return string == string[::-1]

# Create a server socket, bind it to an IP/port, and listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Accept any incoming connection and let them know they are connected
print("Server is running... \n")
client_socket, client_address = server_socket.accept()

# Send a welcome message to the connected client
client_socket.send("You are connected to the server...".encode(ENCODER))

while True:
    # Receive information from the client
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    # Quit if the client socket wants to quit, else display the message
    if message.lower() == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat... goodbye!")
        break
    elif message.startswith('CHECK'):
        _, num, operation = message.split(' ')
        num = int(num)
        if operation == 'prime':
            response = str(check_prime(num))
        elif operation == 'palindrome':
            response = str(check_palindrome(str(num)))
        else:
            response = 'Invalid operation'
        client_socket.send(response.encode(ENCODER))
    elif message.startswith('CAPITALIZE'):
        text_to_capitalize = message.split(' ', 1)[1]
        response = capitalize_text(text_to_capitalize)
        client_socket.send(response.encode(ENCODER))
    else:
        print(f"\n{message}")
        user_input = message
        client_socket.send(user_input.encode(ENCODER))

client_socket.close()
