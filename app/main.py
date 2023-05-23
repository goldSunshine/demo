from flask import Flask, request
from app.demo.urls import bp as demo_bp
from flasgger import Swagger

app = Flask(__name__)

app.register_blueprint(demo_bp)
swagger = Swagger(app, config={"specs_route": "/apidocs"}, merge=True)

if __name__ == '__main__':
    app.run(port=8090, host="0.0.0.0", debug=True)