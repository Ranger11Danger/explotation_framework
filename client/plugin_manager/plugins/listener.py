from plugin_manager.manager import plugin_manager
from cmd2 import with_argparser
import argparse
import socket
import threading

argparser = argparse.ArgumentParser()
argparser.add_argument('-p', help="Port to listen on", required=True)


class test(plugin_manager):

    
    @with_argparser(argparser)
    def do_listen(self, args):
        def listen(setport):
            host = "0.0.0.0"
            port = int(setport)
            s = socket.socket()
            s.bind((host, port))
            s.listen(5)

            while True:
                conn, addr = s.accept()
                print(f"connection from {addr[0]}:{addr[1]}")
                self.addresses.append((addr[0], addr[1]))
                self.connections.append(conn)

        port = args.p
        t = threading.Thread(target=listen, args=[port])
        t.daemon = True
        t.start()
        print(f"Now listening on port {port}")
