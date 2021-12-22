import os
import flask
from werkzeug.utils import secure_filename
port = 5100
app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    file = request.files['filename']
    filename = secure_filename(file.filename)
    file.save(os.path.join("uploads/", filename))
    return "Image Uploaded Successfully"

app.run(host="0.0.0.0", port=port)
