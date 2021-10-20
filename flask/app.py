from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}} )


@app.route('/api/v1.0/mensaje')
def mensaje():
    return "Running Flask server http://127.0.0.1:5000 Prueba NE"

if __name__ == "__main__":
    app.run(debug=True)