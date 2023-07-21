# Assignment: Programming Project: Client-Server Chat/Game
# Author: Maggie Wu

# Citation for the following program:
# Date: 6/01/2023
# Title: Computer networking : a top-down approach
# Author: James F. Kurose
# Based on:
# Source URL: https://search.library.oregonstate.edu/discovery/delivery/01ALLIANCE_OSU:OSU/12325778590001865

from socket import *
import ascii_art

server_host = 'localhost'
server_port = 19991

# Create socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Establish connection between client and server
server_socket.bind((server_host, server_port))
server_socket.listen()

print("Server listening on: ", server_host, "on port: ", server_port)
connection_socket, connection_address = server_socket.accept()
print("Connected by: ", connection_address)
print("Waiting for message.....")
print("Type /q to quit")
print("Enter message to send. Please wait for input prompt before entering message.....")

connected = True
game_active = False
while connected == True:
    # Receive data from the client
    data = connection_socket.recv(1024).decode('utf-8')

    # Check if the client wants to quit
    if data == '/q':
        connected = False
        print("Client has requested shutdown. Shutting down!")
        break

    # Check if the client wants to play rock-paper-scissors
    if data == "play rps":
        print("Now playing Rock-Paper-Scissors!")
        print("You are Player 2")
        print("Please wait for your turn...")
        game_active = True

    # Check if a game is active and the client has made a valid move
    while game_active and (data == 'r' or data == 'p' or data == 's'):
        rps_input = input("Please type 'r', 'p', or 's': ")

        # Validate the user's choice for rock-paper-scissors
        while rps_input.lower() not in ["r","p","s"]:
            print("Only rock, paper, or scissors here. Try again!")
            rps_input = input("Please type 'r', 'p', or 's': ")
            
        print(f"You choose {rps_input}")
        ascii_art.get_ascii(rps_input)
        message = ascii_art.win(data, rps_input)
        print(f"{data} vs {rps_input}")
        print(message)

        # Determine the winner and send the result to the client
        if message == "You win :)":
            connection_socket.sendall(bytes(str(f"{rps_input} vs {data}\nYou lose :("), encoding='utf-8'))
        else:
            connection_socket.sendall(bytes(str(f"{rps_input} vs {data}\nYou win :)"), encoding='utf-8'))

        game_active = False
        data = ""
        continue

    # Check if there is data received from the client and a game is not active
    if len(data) > 0 and not game_active:
        print(f"{data}")
        user_input = input("Enter Input >")

        # Check if the user input is empty
        while user_input == "":
            print("Please enter a message.")
            user_input = input("Enter Input >")

        # Check if the user wants to quit
        if user_input == '/q':
            connected = False
            print("Shutting down!")

        # Send the user input to the client
        connection_socket.sendall(bytes(str(user_input), encoding='utf-8'))

# Close the connection socket and server socket
connection_socket.close()
server_socket.close()
