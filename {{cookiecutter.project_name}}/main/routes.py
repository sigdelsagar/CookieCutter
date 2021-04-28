from flask import Blueprint

main = Blueprint('main',__name__)

@main.route("/",methods=['GET'])
def hello_world():
    return 'Hello, World!'