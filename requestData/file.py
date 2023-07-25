from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'  # Define the folder to save the uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part in the request", 400
    
    file_data = request.files['file']

    if file_data.filename == '':
            return "No selected file", 400
    file_data.save(os.path.join(app.config['UPLOAD_FOLDER'], file_data.filename))
    return "File saved successfully."
    
    

if __name__ == '__main__':
    app.run(debug=True)