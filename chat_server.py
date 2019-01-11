from socket import *
# Importing socket module
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
        \
                                                                    -All CopyRights\n\
                                                                      C.Siva Prasad\n\
                                                                      R170262\n\
                                                                      F-011\n")

print("*"*10, "CHATON PYTHON ", "*"*10)
print(" "*25, "All Copy Rights-C.Siva Prasad(R170262)")
print("\n\n" + str(gethostname()) + " is serving in port 8000.")


host = input("Enter your IP4 address:-")
partner = input("Enter the name of the other person:-")

x = socket(AF_INET,SOCK_STREAM)
# Creating a socket named "x"

# host_name = gethostname()
# Getting the hostname of the server pc

port = 8000
# Port

x.bind((host, port))
# Connecting socket "x" to host_name and port

# print("The pc " + str(host_name) + " is connected to binded to port 8000.\n")

x.listen(1)
# Listening if any clients likes to connect or not
# print("Listening completed client likes to connect.")
print("Waiting for clients to connect.")

connection, address = x.accept()
# If someone likes to connect,then this will accept the request.
# And the connected pc is treated a 'connection' variable here.
print("Request from the client " + str(address) + " is  accepted.")

while True:
    message = str(input("You:"))
    # Inputting the message
    message = message.encode()
    # Encoding message so that the socket can send message in bytes form
    connection.send(message)
    # Sending the message to the client('connection')

    in_message = connection.recv(1024)
    # Receiving the message in bytes form from the connection variable.
    in_message = in_message.decode()
    # Decoding the message from bytes to characters.
    print(partner, ":", in_message)
    # Printing received message.
x.close()







