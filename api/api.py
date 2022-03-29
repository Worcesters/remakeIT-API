from os import getenv
import logging
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv


load_dotenv()
SECRET_KEY = getenv('SECRET_KEY')

def create_app():
    """
    Function that creates our Flask application...
    """

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("we_api.log"), logging.StreamHandler()]
    )

    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = SECRET_KEY

    @app.route('/', methods=['GET', 'POST'])
    def index():
        return 'Hello World'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)