import socket
import sys
# import nltk
# import threading

# ------------------------------------------------------------------------

class Client():
    def __init__(self):
        self.address_family = socket.AF_INET
        self.socket_type = socket.SOCK_STREAM
        self.sock = socket.socket(self.address_family, self.socket_type)
        self.connected = False

    def connect(self, server, port):
        if self.connected is False:
            self.port = port
            self.server = server
            self.sock.connect((self.server, self.port))
            self.connected = True
            #Todo Note, if the connection establishment failed, the client application should provide a useful error message to the user
            return(f"Connection to MSRG Echo server established: / {self.server} /  {self.port}")
        else:
            return("Already connected")

    def disconnect(self):
        try:
            self.sock.close()
            self.connected = False
            return(f"Connection terminated: /{self.server} / {self.port}")
            #Todo Note that the connection might also be lost due to a connection error or a breakdown of the server
        except:
            return("No connection active")

    def send_messages(self, tokens):
        if self.connected is True:
            delimiter = ' '
            message = delimiter.join(tokens)
            self.sock.sendall(message.encode())

            # data = self.sock.recv(1024)  # Number of bytes we are waiting
            # buffer = data.decode()
            # return (f"Received: {buffer}")
            return self.receive_message()
        else:
            return("No connection active")

    def receive_message(self):
        data = self.sock.recv(1024)  # Number of bytes we are waiting
        buffer = data.decode()
        return (buffer.strip())


    def listener(self): # For the future, not active
        self.listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener_socket.bind('localhost', 1234)
        self.listener_socket.listen(1)
        connection, client_address = self.listener_socket.accept()
        print('Accepted connection from {}:{}'.format(*client_address))
        # receive messages from the client
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print("Listener --> ", data.decode('utf-8'))
            except:
                break
# ------------------------------------------------------------------------
class Command_line_shell():
    def __init__(self):
        self.cli_output("Welcome to the CLI of the client")

    def command_help(self):
        self.cli_output("Welcome to the CLI. Available commands: ")
        print("\tconnect: to connect to a server. Arg: Server+port")
        print("\tdisconnect: to disconnect from a server")
        print("\tsend: to send a message. Arg: the message")
        print("\tlog: on process")
        print("\thelp: displays this message")
        print("\tquit: quits the program")

    def command_exit(self):
        self.cli_output("Goodbye!")
        sys.exit(0)

    def cli_output(self, *args):
        if len(args) != 0:
            sys.stdout.write(f"EchoClient> {' '.join(str(arg) for arg in args)}")
            sys.stdout.write('\n')


    def user_input(self):
        cli_input = input("EchoClient>").split()
        self.command = []
        for word in cli_input:
            self.command.append(word)


# ----------------------------------------------------------------------------
def main():
    CLI = Command_line_shell()
    socket_to_server = Client()

    server='cdb.dis.cit.tum.de'
    port=5551

    while True:
        CLI.user_input() # List of tokens

        if CLI.command[0] == "connect":
            if len(CLI.command) != 3:
                CLI.cli_output("connect command needs 2 arguments: server + port")
            elif len(CLI.command) == 3:
                CLI.cli_output(socket_to_server.connect(CLI.command[1], int(CLI.command[2])))
                CLI.cli_output(socket_to_server.receive_message())

        elif CLI.command[0] == "disconnect":
            if len(CLI.command)== 1:
                CLI.cli_output(socket_to_server.disconnect())
            elif len(CLI.command) != 1:
                CLI.cli_output("disconnect command doesn't accepts arguments")

        elif CLI.command[0] == "send":
            if len(CLI.command) > 1:
                CLI.cli_output(socket_to_server.send_messages(CLI.command[1:]))
            elif len(CLI.command) == 1:
                CLI.cli_output("send command needs 1 argument at least")

        elif CLI.command[0] == "logLevel":
            pass
        elif CLI.command[0] == "help":
            CLI.command_help()
        elif CLI.command[0] == "quit":
            CLI.command_exit()
        else:
            CLI.cli_output("Invalid command. Type 'help' for a list of available commands.")

# ----------------------------------------------------------------------------

if __name__ == '__main__':
    main()

