from flask import Flask
from routes.usuarios import usuarios_bp
import config

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(usuarios_bp)

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], port=app.config["PORT"])