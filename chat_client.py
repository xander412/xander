from socket import *
# Importing the socket
with open("Instructions.txt", "w") as inst:
    inst.write("INSTRUCTIONS:-\n\
        *This chatting app is terminal to terminal chatting application.\n\
        *Two persons may chat through this application through this LAN.\n\
        *One must run Chaton_server.exe and the other must run Chaton _client.exe.\n\
                                                \n\
                                                \n\
        MANDATORY    INSTRUCTIONS:-\n\
        *Those  who  opened  Chaton_server.exe  must  first  run  the  app  &  and  then  the client.\n\
            *As  this  is  a type  send-receive  chat server\n\
                >>>One  must  wait  until  they get  the reply\n\
                    That means you must not send any message until you get the following code\n\
                        You:\n\
        *Server must not run this application if  the IP  is already  being  used.\n\
        \n\
                                                                    -All CopyRights\n\
                                                                      C.Siva Prasad\n\
                                                                      R170262\n\
                                                                      F-011\n")
print("*"*10, "CHATON PYTHON ", "*"*10)
print(" "*25, "All Copy Rights-C.Siva Prasad(R170262)")

partner = str(input("\n\nEnter the name of the person other person:-"))
x = socket(AF_INET, SOCK_STREAM)
# Creating a socket

host_name = str(input("Enter the server name:-"))
# Client is asked to enter the server name

port = 8000
# Declaring the port

x.connect((host_name, port))
# Connecting or binding the client to the host and port

while True:

    in_message = x.recv(1024)
    # Receiving the message in bytes form.
    in_message = in_message.decode()
    # Decoding the message from bytes to characters
    print(partner, ":", in_message)
    # Printing received message.
    message = str(input("You:"))
    # Inputting the message
    message = message.encode()
    # Encoding message so that the socket can send message in bytes form
    x.send(message)
    # Sending the message
x.close()

