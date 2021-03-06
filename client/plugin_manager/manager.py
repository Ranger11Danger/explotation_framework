plugin_list = {}
import importlib
import os

class plugin_manager():
    
    def __init_subclass__(cls):
        
        func_list = dir(cls)
        for name in func_list:
            if name[:3] == "do_":
                plugin_list[cls.__dict__[name].__name__] = cls.__dict__[name]
        

    def import_plugins(self):
        for item in os.listdir("plugin_manager/plugins"):

            try:
                importlib.import_module(f"plugin_manager.plugins.{item[:-3]}")
            except:
                pass

    def install_plugins(self, my_class):
        
        for k,v in plugin_list.items():
            setattr(my_class,k,v)

    def __init__(self, my_class):
        self.import_plugins()
        self.install_plugins(my_class)
