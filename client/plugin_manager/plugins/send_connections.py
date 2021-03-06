from plugin_manager.manager import plugin_manager
from cmd2 import with_argparser
import argparse
import socket
import threading

argparser = argparse.ArgumentParser()
argparser.add_argument('-d', help="data to send", required=True)


class test(plugin_manager):

    
    @with_argparser(argparser)
    def do_send(self, args):
        self.connections[int(self.current_session)].send(str(args.d).encode())
