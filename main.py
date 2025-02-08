from flask import Flask, request,render_template,jsonify
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = "static/uploads"
try:
   print("Creating the directory ...")
   os.makedirs(UPLOAD_FOLDER, exist_ok=True)
except:
   print("Directory has been created")

@app.route("/")
def index():
     return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    image = request.files['image']
    image_path = os.path.join(UPLOAD_FOLDER, "captured_image.jpg")
    image.save(image_path)
    
    return jsonify({"message": "Image saved", "path": image_path})

if __name__ == '__main__':
       app.run(ssl_context='adhoc',debug=True,threaded=True,host="0.0.0.0", port=5000)
