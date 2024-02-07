import random
import socket

HOST_IP = '192.168.0.194'
HOST_PORT = 50001
ENCODER = "utf-8"
BYTESIZE = 1024
DEFAULT_PIN = '1234'  # Set a default PIN
DEFAULT_USERNAME = 'user123'  # Set a default username

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

print("Server is running... \n")
client_socket, client_address = server_socket.accept()

# Set a username and PIN for the server
server_username = DEFAULT_USERNAME
server_pin = DEFAULT_PIN

# Send a message to the client to provide username and PIN
client_socket.send("provide_credentials".encode(ENCODER))

while True:
    # Receive username and PIN from the client
    credentials = client_socket.recv(BYTESIZE).decode(ENCODER)
    entered_username, entered_pin = credentials.split()

    if entered_username == server_username and entered_pin == server_pin:
        client_socket.send("Credentials verified. You can now perform transactions.".encode(ENCODER))
        break
    else:
        client_socket.send("Invalid credentials. Please try again.".encode(ENCODER))

balance = 50000

while True:
    op = client_socket.recv(BYTESIZE).decode(ENCODER)
    print('Requested operation: ', op)

    error = random.randint(1, 10)

    if op == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nThanks for taking our service.")
        break
    elif error <= 5:
        print('Error Generated!!\n')
        client_socket.send("Error".encode(ENCODER))
        break
    else:
        amount = client_socket.recv(BYTESIZE).decode(ENCODER)
        print('Amount: ', amount)
        if op == 'wd':
            if balance < int(amount):
                client_socket.send("You have insufficient funds!!".encode(ENCODER))
                print('Insufficient fund responded')
            else:
                balance -= int(amount)
                response = "Amount withdrawn: " + str(amount) + "\nBalance: " + str(balance)
                client_socket.send(response.encode(ENCODER))
                print('Successful withdrawal responded')
        elif op == 'dp':
            balance += int(amount)
            response = "Amount deposited: " + str(amount) + "\nBalance: " + str(balance)
            client_socket.send(response.encode(ENCODER))
            print('Successful deposition responded')

server_socket.close()
