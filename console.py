#!/usr/bin/python3
"""
    Class HBNB Command that defines and execute 
    the console
"""
import cmd
import models
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Defines the HBNB command interpreter.
    
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program

        """
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_help(self, arg):
        """Display helpful messages"""
        super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
