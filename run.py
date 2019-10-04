from flask import Flask
from flask_restful import  Api
from flask_restful_swagger import swagger
from flasgger import Swagger, swag_from

app = Flask(__name__)


# swagger config


def create_app(config_filename):
    app = Flask(__name__,static_folder='/static')
    app.config.from_object(config_filename)
    app.config['SWAGGER'] = {
        'title': 'Flasgger RESTful',
        'uiversion': 2
    }
    swag = Swagger(app)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
