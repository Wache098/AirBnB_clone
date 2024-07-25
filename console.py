#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project.

    Attributes:
        prompt (str): The command prompt string.
    """

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id.

        Args:
            arg (str): The name of the class to create an instance of.

        Example:
            (hbnb) create BaseModel
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
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
        elif args[0] not in HBNBCommand.__classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = storage.all().get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id.

        Args:
            arg (str): The class name and id of the instance to delete.

        Example:
            (hbnb) destroy BaseModel 1234-1234-1234
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Show all instances, or all instances of a class.

        Args:
            arg (str): The class name to show instances of, or empty to show all.

        Example:
            (hbnb) all BaseModel
            (hbnb) all
        """
        args = arg.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__classes():
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            obj_list = [str(obj) for obj in objects.values() if len(args) == 0 or args[0] == obj.__class__.__name__]
            print(obj_list)

    def do_update(self, arg):
        """Update an instance based on class name and id by adding or updating an attribute.

        Args:
            arg (str): The class name, id, attribute name, and attribute value.

        Example:
            (hbnb) update BaseModel 1234-1234-1234 name "My New Name"
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = storage.all().get(key)
            if obj:
                setattr(obj, args[2], args[3].strip('"'))
                obj.save()
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    @staticmethod
    def __classes():
        """Returns the list of valid classes"""
        return {"BaseModel", "User", "State", "City", "Place", "Amenity", "Review"}


if __name__ == "__main__":
    HBNBCommand().cmdloop()
