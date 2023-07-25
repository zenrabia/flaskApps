from flask import Flask, request, flash, send_file
from wave_example import infos
from processing_volume import increase_volume, volume
import os
from pydub import AudioSegment


UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Allowed audio file extensions
ALLOWED_EXTENSIONS = {"wav"}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/get_params', methods=['POST'])
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
            path=os.path.join(UPLOAD_FOLDER, filename)
            file.save(path)
            return str(infos(path))
        

@app.route('/get_volume', methods=['POST'])
def get_volume():
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
            path=os.path.join(UPLOAD_FOLDER, filename)
            file.save(path)
            return str(volume(path))
        

@app.route('/increase_volume', methods=['POST'])
def process_vol():
    if request.method == 'POST':
        if "file" not in request.files:
            # flash("file not found")
            return "no wave file to return"
        
        file = request.files["file"]

        if file.filename == ' ':
            # flash("empty filename")
            return "no filename to return"
        

        if file.filename.endswith(".wav"):
            filename = file.filename
            input_path = os.path.join(UPLOAD_FOLDER, filename)
            output_path = os.path.join(UPLOAD_FOLDER, "processed_"+filename)
            print("---------------------------",output_path)
            file.save(input_path)

            #increase the volume
            processed_audio = increase_volume(input_path)

            # Save the processed audio
            processed_audio.export(output_path, format="wav")
            return str(volume(input_path)) + "\n\t" + str(volume(output_path))
            return "volume increased !"

if __name__ == "__main__":
    app.run(debug=True)