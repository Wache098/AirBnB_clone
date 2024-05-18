#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from storage.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project.

    Attributes:
        prompt (str): The command prompt string.
        storage (FileStorage): An instance of the FileStorage class to handle
            serialization and deserialization of instances.
    """

    prompt = "(hbnb) "
    storage = FileStorage()
    storage.reload()

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id.

        Args:
            arg (str): The name of the class to create an instance of.

        Example:
            (hbnb) create BaseModel
        """
        if arg == "BaseModel":
            new_instance = BaseModel()
            self.storage.new(new_instance)
            self.storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show an instance based on class name and id.

        Args:
            arg (str): The class name and id of the instance to show.

        Example:
            (hbnb) show BaseModel 1234-1234-1234
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = self.storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program.

        Args:
            arg (str): The argument passed to the command, not used here.

        Returns:
            bool: True to exit the command loop.
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program.

        Args:
            arg (str): The argument passed to the command, not used here.

        Returns:
            bool: True to exit the command loop.
        """
        return True
