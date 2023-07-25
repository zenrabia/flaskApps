from flask import Flask, request, flash
from wave_example import infos
import os

UPLOAD_FOLDER = './uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/mywave', methods=['POST'])
def get_wave_info():
    if request.method == 'POST':
        if "file" not in request.files:
            flash("file not found")
            return "no wave file to return"
        
        file = request.files["file"]

        if file.filename == ' ':
            flash("empty filename")
            return "no filename to return"
        

        if file.filename.endswith(".wav"):
            filename = file.filename
            path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            return str(infos(path))

if __name__ == "__main__":
    app.run(debug=True)