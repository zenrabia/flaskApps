from flask import Flask, request, flash, send_file, jsonify
from wave_example import infos
from processing_audio import increase_volume, volume, segmenter, remove_noise, remove_noise2
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
        
@app.route('/seg_audio', methods=['POST'])
def process_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No audio file found'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected audio file'}), 400

    if file.filename.endswith(".wav"):
            filename = file.filename
            input_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(input_path)

            try:
                
                segments = segmenter(input_path,segment_duration = 1000)

                output_path = 'uploads/output_audio_segments'
                if not os.path.exists(output_path):
                    os.makedirs(output_path)

                # Sauvegarder les segments audio dans le répertoire
                for i, segment in enumerate(segments):
                    output_file = os.path.join(output_path, f'{filename[:-4]}__{i}.wav')
                    segment.export(output_file, format='wav')

                return jsonify({'message': 'Audio processed successfully', 'output_dir': output_path}), 200
    
            except Exception as e:
                return jsonify({'error': str(e)}), 500
            

# @app.route('/rm_noise', methods=['POST'])
# def rm_noise():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No audio file found'}), 400

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected audio file'}), 400
    
#     if file.filename.endswith(".wav"):
#             filename = file.filename
#             input_path = os.path.join(UPLOAD_FOLDER, filename)
#             file.save(input_path)

#             try:
                
#                 # Remove noise from the audio
#                 processed_audio = remove_noise(input_path, threshold = 400)

#                 # Save the processed audio
#                 output_file = f'uploads/{filename[:-4]}_NoNoise.wav'
#                 processed_audio.export(output_file, format='wav')

#                 return jsonify({'message': 'Noise removed successfully !', 'output_file': output_file}), 200
#             except Exception as e:
#                 return jsonify({'error': str(e)}), 500

# @app.route('/rm_noise', methods=['POST'])
# def rm_noise():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No audio file found'}), 400

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected audio file'}), 400
    
#     if file.filename.endswith(".wav"):
#             filename = file.filename
#             input_path = os.path.join(UPLOAD_FOLDER, filename)
#             file.save(input_path)

#             try:
                
#                 # Remove noise from the audio
#                 processed_audio = remove_noise2(input_path)

#                 # Save the processed audio
#                 output_file = f'uploads/{filename[:-4]}_NoNoise.wav'
#                 processed_audio.save(output_file)
                
#                 return jsonify({'message': 'Noise removed successfully !', 'output_file': output_file}), 200
#             except Exception as e:
#                 return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)