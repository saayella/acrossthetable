from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})