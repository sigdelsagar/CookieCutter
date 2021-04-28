import logging
import os
import config
from flask import Flask

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()

# print(config.as_dict())

def create_app():
    logger.info(f'Starting app in {config.APP_ENV} environment')
    app = Flask(__name__)
    app.config.from_object("config")

    from main.routes import main
    import command

    #register your blue print here
    app.register_blueprint(main)
    app.register_blueprint(command._app)
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)