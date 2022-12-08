from os import environ

from main import app

if __name__ == "__main__":
    host = environ.get('IP_ADDRESS', default='127.0.0.1')
    app.run(host=host, port=81)