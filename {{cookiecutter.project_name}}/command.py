import os
import click
from flask import Blueprint

_app = Blueprint('start', __name__)

@_app.cli.command('app')
@click.argument('name')
def create_new_app(name):
    """ Creates a app """
    print("Create app: {}".format(name)) 
    try:
        os.mkdir(name)
        initfile = os.path.join(name, "__init__.py")
        file = open(initfile, "w")
        file.close()

        routes = os.path.join(name, "routes.py")
        file1 = open(routes, "w")
        file1.write("from flask import Blueprint\n")
        file1.write("\n{} = Blueprint('{}',__name__)\n".format(name,name))
        file1.write("\n#@{}.route('/'',methods=['GET'])\n#def view1():\n    #return 'Hello World' ".format(name))
        file1.close()

        models = os.path.join(name, "models.py")
        file = open(models, "w")
        file.write("#Your models here\n")
        file.close()

    except FileExistsError as exe:
        print(exe)