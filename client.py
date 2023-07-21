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
client_socket = socket(AF_INET, SOCK_STREAM)

# Establish connection between client and server
client_socket.connect((server_host, server_port))
print("Connected to: ", server_host, "on port: ", server_port)
print("Type /q to quit")
print("Enter message to send. Please wait for input prompt before entering message.....")
print("Note: Type 'play rps' to start a game of rock-paper-scissors")

connected = True
while connected == True:
    game_active = False
    user_input = input("Enter Input >")

    # Check if the user input is empty
    if user_input == "":
        print("Please enter a message.")
        continue

    # Check if the user wants to quit
    if user_input == '/q':
        connected = False
        print("Shutting down!")

    # Check if the user wants to play rock-paper-scissors
    if user_input == "play rps":
        # Send the user input to the server
        client_socket.sendall(bytes(str(user_input), encoding='utf-8'))
        print("Now playing Rock-Paper-Scissors!")
        print("You are Player 1")
        game_active = True
        rps_input = input("Please type 'r', 'p', or 's': ")

        # Validate the user's choice for rock-paper-scissors
        while rps_input.lower() not in ["r","p","s"]:
            print("Only rock, paper, or scissors here. Try again!")
            rps_input = input("Please type 'r', 'p', or 's': ")
            
        print(f"You choose {rps_input}")
        ascii_art.get_ascii(rps_input)
        print("Please wait for Player 2")

        # Send the user's choice to the server
        client_socket.sendall(bytes(str(rps_input), encoding='utf-8'))

        # Receive and print the server's response
        print(client_socket.recv(1024).decode('utf-8'))
        continue

    # Check if a game is not active
    if not game_active:
        # Send the user input to the server
        client_socket.sendall(bytes(str(user_input), encoding='utf-8'))
        # Receive data from the server
        data = client_socket.recv(1024).decode('utf-8')

    # Check if the server requested shutdown
    if data == '/q':
        connected = False
        print("Server has requested shutdown. Shutting down!")
        break

    # Check if there is data received from the server and a game is not active
    if len(data) > 0 and not game_active:
        print(f"{data}")

# Close the client socket
client_socket.close()
