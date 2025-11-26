import os
import sys
from flask import Flask, render_template

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.append(ROOT)

# Import blueprint (now that sys.path contains project root)
# from Backend.routes.resume_routes import resume_routes

# --- base directories ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'frontend', 'templates')
STATIC_FOLDER = os.path.join(BASE_DIR, 'frontend', 'static')

# --- Initialize Flask app ---
app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)

# --- Register the blueprint ---
# app.register_blueprint(resume_routes)

# --- Default route ---
@app.route('/')
def home():
    return render_template('index.html')

# --- Run app ---
if __name__ == '__main__':
    app.run(debug=True)

