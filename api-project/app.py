from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db  
from routes.bogie_checksheet import bogie_bp
from models.model import KPAForm
from routes.wheel_specifications import wheel_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app) 
CORS(app)

from routes.api1 import api1_bp

app.register_blueprint(wheel_bp, url_prefix="/")
app.register_blueprint(bogie_bp, url_prefix="/")
app.register_blueprint(api1_bp, url_prefix="/api/v1/api1")

@app.route("/")
def home():
    return {"message": "KPA API is running 🚀"}

if __name__ == "__main__":
    app.run(debug=True)
