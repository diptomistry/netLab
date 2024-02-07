import socket

DEST_IP = '192.168.0.194'
DEST_PORT = 50001
ENCODER = "utf-8"
BYTESIZE = 1024

# Create a client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

while True:
    # Receive information from the server
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    if message == "provide_credentials" or message == "Invalid credentials. Please try again.":
        # If the server requests credentials, get username and PIN from the user
        if message == "Invalid credentials. Please try again.":
            credentials_input = input("Invalid credentials. Try again. \nEnter username and PIN separated by space: ")
        else:
            credentials_input = input("Enter username and PIN separated by space: ")
        client_socket.send(credentials_input.encode(ENCODER))

    elif message == "Credentials verified. You can now perform transactions.":
        print(f"\n{message}")
        while True:
            # Add operation input (withdrawal/deposit)
            operation_input = input("Enter operation (wd/dp or quit): ")

            client_socket.send(operation_input.encode(ENCODER))

            if operation_input.lower() == 'quit':
                break

            user_input = input("Enter amount: ")
            client_socket.send(user_input.encode(ENCODER))

            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            print(f"\n{message}")
            if message == "Error":
                break
            else:

                # Check if the user wants to perform another operation
                another_operation = input("Do you want to perform another operation? (yes/no): ")
                if another_operation.lower() != 'yes':
                    client_socket.send("quit".encode(ENCODER))
                    break

# Close the client socket
client_socket.close()
