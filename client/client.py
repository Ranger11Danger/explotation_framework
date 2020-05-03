#!/usr/bin/python3

from cmd2 import Cmd, with_argparser
from plugin_manager.manager import plugin_manager

class interpreter(Cmd):
    intro = "welcome to my rat"
    prompt = "> "
    addresses = []
    connections = []
    current_session = 0

manager = plugin_manager(interpreter)

session = interpreter()
session.cmdloop()