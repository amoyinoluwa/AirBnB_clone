#!/usr/bin/python3
"""
The HBNB command console
Version: 1.0
"""


from models.base_model import BaseModel
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class is a limited-use command
    line interpreter for manipulating objects
    """

    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance of BaseModel and prints the id"""
        if not arg:
            print("** class name missing **")
        else:
            if arg not in globals():
                print("** class doesn't exist **")
            else:
                newObject = eval(arg)()
                newObject.save()
                print(newObject.id)

    def do_show(self, arg):
        """Prints the string representation of
        an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            if not args[0] in globals():
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            if not args[0] in globals():
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute"""
        if not arg:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            argCount = len(args)
            if not args[0] in globals():
                print("** class doesn't exist **")
            elif argCount == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    if argCount == 2:
                        print("** attribute name missing **")
                    elif argCount == 3:
                        print("** value missing **")
                    else:
                        obj = models.storage.all()[key]
                        arg = args[3]
                        if '.' in arg:
                            try:
                                arg = float(arg)
                            except ValueError:
                                pass
                        else:
                            try:
                                arg = int(arg)
                            except ValueError:
                                pass
                        setattr(obj, args[2], arg)
                        models.storage.save()
                else:
                    print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Extra command that exits the program"""
        return True

    def emptyline(self):
        pass

    def do_all(self, arg):
        """Prints string representations of instances"""
        if not arg:
            print([str(_class) for _, _class in models.storage.all().items()])
        else:
            result = []
            for key in models.storage.all():
                currClass = key.split('.')[0]
                if currClass == arg:
                    result.append(str(models.storage.all()[key]))
            if not result:
                print("** class doesn't exist **")
            else:
                print(result)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
