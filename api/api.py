from os import getenv
import logging
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from dotenv import load_dotenv
from werkzeug.utils import secure_filename


load_dotenv()
SECRET_KEY=getenv('SECRET_KEY')
PORT=getenv('PORT')
HOST='0.0.0.0'
BASE_URL='/api/v1'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'gif'}

def allowed_file(filename):
    """
    Function that checks if the file is allowed
    """
    extension = filename.rsplit('.', 1)[1].lower()
    if extension in ALLOWED_EXTENSIONS:
        return True
    else: 
        return False

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
        
    @app.route(f'{BASE_URL}/upload', methods=['POST'])
    def upload():
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
            filename = secure_filename(file.filename)
            return jsonify(
                message={
                    'fr': "Fichier envoyé avec succès!",
                    'en': "File sent successfully!"
                },
                error=False,
                file="{}".format(file.filename)
            ), 200
        
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