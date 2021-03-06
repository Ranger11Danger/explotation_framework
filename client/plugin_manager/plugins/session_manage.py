from plugin_manager.manager import plugin_manager
from cmd2 import with_argparser
import argparse
import socket
import threading
from tabulate import tabulate

base_parser = argparse.ArgumentParser()
base_subparsers = base_parser.add_subparsers(title='subcommands', help='subcommand help')

parser_select = base_subparsers.add_parser('select', help='select sessions')
parser_detach = base_subparsers.add_parser('detach', help='detach from current sessions')
parser_list = base_subparsers.add_parser('list', help="show current sessions")

parser_select.add_argument('session_number', help='Session to select')



class test(plugin_manager):

    def base_select(self, args):
        """select session"""
        try:
            self.connections[int(args.session_number)]
            self.current_session = args.session_number
            self.prompt = f'Session: {self.current_session}> '

        except:
            print("session doesn't exist")

    def base_detach(self, args):
        self.current_session = None
        self.prompt = "> "

    def base_list(self, args):
        headers= ["session number", "ip", "port"]
        print(tabulate(self.addresses, headers=headers, showindex="always",disable_numparse=True))
    
    parser_select.set_defaults(func=base_select)
    parser_detach.set_defaults(func=base_detach)
    parser_list.set_defaults(func=base_list)
    
    @with_argparser(base_parser)
    def do_session(self, args):
        func = getattr(args, 'func', None)
        if func is not None:
            # Call whatever subcommand function was selected
            func(self, args)
        else:
            # No subcommand was provided, so call help
            self.do_help('session')
