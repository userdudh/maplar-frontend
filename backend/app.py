from flask import Flask
from flask_cors import CORS
from crud import imoveis_bp
import bd

app = Flask(__name__)

CORS(app)

app.register_blueprint(imoveis_bp, url_prefix="/api")

@app.route("/")
def home():
    return "API rodando"

if __name__ == "__main__":
    bd.Base.metadata.create_all(bind=bd.db)
    
    app.run(debug=True)