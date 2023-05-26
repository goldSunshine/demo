from flasgger import Swagger
from flask import Flask

from app.demo.urls import bp as demo_bp
from app.extensions import JSONEncoder, MyResponse

app = Flask(__name__)

app.register_blueprint(demo_bp)
app.json_encoder = JSONEncoder
app.response_class = MyResponse
swagger = Swagger(app, config={"specs_route": "/apidocs"}, merge=True)

if __name__ == "__main__":
    app.run(port=8090, host="0.0.0.0", debug=True)
