from os import getenv
import logging
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from dotenv import load_dotenv


load_dotenv()
SECRET_KEY=getenv('SECRET_KEY')
PORT=getenv('PORT')
HOST='0.0.0.0'
BASE_URL='/api/v1'

def create_app():
    """
    Function that creates our Flask application...
    """

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("api/remakeIT_api.log"), logging.StreamHandler()]
    )

    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = SECRET_KEY
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        """
        Redirect to the BASE_URL
        """
        return redirect(BASE_URL, code=302)

    @app.route(f'{BASE_URL}/', methods=['GET', 'POST'])
    def welcome():
        return jsonify(
            message="Welcome to the Remake IT API!",
            version="0.1.0",
            authors=[
                {
                    'name': 'Théo BIET',
                    'github': 'https://github.com/TheoBIET',
                },
                {
                    'name': 'Éric Clouzet',
                    'github': 'https://github.com/EricClouzet',
                },
                {
                    'name': 'Mickael Milliat',
                    'github': 'https://github.com/mm-devpro',
                },
                {
                    'name': 'Jérémy',
                    'github': 'https://github.com/Worcesters',
                }
            ]
        )

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host=HOST, port=PORT, debug=True)