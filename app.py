import logging

from os import getenv
from flask import Flask, request, jsonify, redirect, make_response
from flask_cors import CORS
from dotenv import load_dotenv

from classes.ImageHandler import ImageHandler
from utils.constants import HOST, BASE_URL, AUTHORS, ALLOWED_EXTENSIONS, ALLOWED_FILTERS
from utils.func import allowed_file, allowed_filter, c_is_valid, allowed_extension

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
        handlers=[logging.FileHandler(
            "remakeIT_api.log"), logging.StreamHandler()]
    )

    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = SECRET_KEY

    @app.route('/')
    def redirect_to_base_url():
        return redirect(BASE_URL)

    @app.route(f'{BASE_URL}/', methods=['GET', 'POST'])
    def welcome():
        return jsonify(
            message="Welcome to the Remake IT API!",
            version="0.1.0",
            authors=AUTHORS
        )

    @app.route(f'{BASE_URL}/download', methods=['POST', 'GET'])
    def download_new_file():
        # Arguments de l'URL
        t_args = {k: v for k, v in request.args.items()}

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
        if allowed_file(file.filename):
            image = ImageHandler(file)

            if "filter" in t_args:
                filter = t_args["filter"]
                if(allowed_filter(filter)):
                    image.set_filter(filter)
                else:
                    return jsonify(
                        message={
                            'fr': f"Le filtre {filter} n'est pas reconnu.",
                            'en': f"The filter {filter} is not recognized.",
                        },
                        filters=ALLOWED_FILTERS,
                        error=True,
                    ), 400
            if "compression" or "weight" or "width" in t_args:
                h = int(t_args['height']) if "height" in t_args else None
                w = int(t_args['width']) if "width" in t_args else None
                c = int(t_args['compression']
                        ) if "compression" in t_args else None

                if c:
                    if not c_is_valid(c):
                        return jsonify(
                            message={
                                'fr': "La compression choisie n'est pas valide. Elle doit être comprise entre 0 et 100.",
                                'en': "The compression chosen is not valid. It must be between 0 and 100.",
                            },
                            error=True,
                        ), 400

                print('Set dimensions')
                image.set_dimensions_and_compression(h, w, c)

            if "extension" in t_args:
                ext = t_args['extension']
                if(allowed_extension(ext)):
                    image.set_ext(ext)
                else:
                    return jsonify(
                        message={
                            'fr': "L'extension cible n'est pas autorisée",
                            'en': "Target extension is not allowed",
                        },
                        error=True,
                        allowed_extensions=[ext for ext in ALLOWED_EXTENSIONS],
                        file="{}".format(file.filename)
                    ), 400

            response = make_response(image.encoded)
            response.headers['Content-Type'] = f'image/{image.target_extension}'

            return response
        else:
            return jsonify(
                message={
                    'fr': "Le fichier n'est pas autorisé",
                    'en': "The file is not allowed"
                },
                error=True,
                allowed_extensions=[ext for ext in ALLOWED_EXTENSIONS],
                file="{}".format(file.filename)
            ), 400

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host=HOST, port=PORT, debug=True)
