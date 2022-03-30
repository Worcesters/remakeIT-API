import logging
import numpy as np
import cv2

from os import getenv
from flask import Flask, request, jsonify, redirect, render_template, send_from_directory, make_response
from flask_cors import CORS
from dotenv import load_dotenv
from functools import wraps
from werkzeug.utils import secure_filename

from classes.ImageHandler import ImageHandler
from utils.constants import ALLOWED_EXTENSIONS, HOST, BASE_URL
from utils.func import allowed_file

load_dotenv()
SECRET_KEY = getenv('SECRET_KEY')
PORT = getenv('PORT')


def create_app():
    """
    Function that creates our Flask application...
    """

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("remakeIT_api.log"), logging.StreamHandler()]
    )

    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = SECRET_KEY

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
        
    @app.route(f'{BASE_URL}/convert', methods=['POST'])
    def convert():
        if 'file' not in request.files:
            return jsonify(
                message={
                    'fr': "Aucun fichier n'a été envoyé.",
                    'en': "No file has been sent.",
                },
                error=True,
            ), 400
            return redirect(request.url)
        
        file = request.files['file']
        extension_target = request.form.get('extension')
        
        if allowed_file(file.filename) & allowed_file(f'.{extension_target}'):
            img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
            _, img_encoded = cv2.imencode(f'.{extension_target}', img)
            response = make_response(img_encoded.tobytes())
            response.headers['Content-Type'] = f'image/{extension_target}'
            return response
        
        return jsonify(
            message={
                'fr': "Le fichier n'est pas autorisé",
                'en': "The file is not allowed"
            },
            error=True,
            allowed_extensions=[ext for ext in ALLOWED_EXTENSIONS],
            file="{}".format(file.filename)
        ), 400       

    @app.route(f'{BASE_URL}/download', methods=['POST', 'GET'])
    def download_new_file():
        # Arguments de l'URL
        t_args = {k: v for k, v in request.args.items()}
        file = request.files['file']
        if allowed_file(file.filename):
            image = ImageHandler(file)

            if "extension" in t_args:
                image.set_ext(t_args['extension'])

            if "filter" in t_args:
                image.set_filter(t_args['filter'])

            response = make_response(image.encoded)
            response.headers['Content-Type'] = f'image/{image.target_extension}'

            return response

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host=HOST, port=PORT, debug=True)
