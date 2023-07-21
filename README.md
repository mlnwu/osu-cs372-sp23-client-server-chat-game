# Client-Server Chat/Game
In this coding project you will first create a simple client-server chat room between a
client and a server program. This requires knowledge of socket programming and general
TCP considerations.
Later, your task is to design and implement a multiplayer ASCII game (any game) within
the chat programs between the client and server. This is to give you the opportunity to
experiment with more complicated procedures for sending information to and from the
client/server.

## Specification

### Server

1. The server creates a socket and binds to ‘localhost’ and port xxxx
2. The server then listens for a connection
3. When connected, the server calls recv to receive data
4. The server prints the data, then prompts for a reply
5. The server sends the reply
6. Back to step 3
7. Sockets are closed (can use with in python3)

### Client

1. The client creates a socket and connects to ‘localhost’ and port xxxx
2. When connected, the client prompts for a message to send
3. The client sends the message
4. The client calls recv to receive data
5. The client prints the data
6. Back to step 2
7. Sockets are closed (can use with in python3)
