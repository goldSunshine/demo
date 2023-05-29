from flasgger import Swagger
from flask import Flask, request

from app.demo.urls import bp as demo_bp
from app.extensions import JSONEncoder, MyResponse, get_loghandler

app = Flask(__name__)

app.register_blueprint(demo_bp)
app.json_encoder = JSONEncoder
app.response_class = MyResponse
app.logger.addHandler(get_loghandler())
swagger = Swagger(app, config={"specs_route": "/apidocs"}, merge=True)


@app.before_request
def log_request():
    app.logger.info(f'{request.method} {request.path} {request.remote_addr}')


if __name__ == "__main__":
    app.run(port=8090, host="0.0.0.0", debug=True)
