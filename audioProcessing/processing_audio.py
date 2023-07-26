from pydub import AudioSegment
import numpy as np
import noisereduce as nr
from scipy.io import wavfile as wav

def volume(path):
    audio = AudioSegment.from_file(path)
    # Calculate the root mean square (RMS) of the audio, which represents the volume
    samples = np.array(audio.get_array_of_samples())
    rms = np.sqrt(np.mean(np.square(samples)))
    return rms

def increase_volume(path):
    # Example audio processing - Increase volume by 10 dB
    audio = AudioSegment.from_file(path)
    processed_audio = audio + 10
    return processed_audio 

def segmenter(path, segment_duration):
    # Charger l'audio avec pydub
    audio = AudioSegment.from_file(path)
    # Diviser l'audio en segments de duree = duree en milliseconds
    segments = [audio[start:start+segment_duration] for start in range(0, len(audio), segment_duration)]
    print("length audio :  ",len(audio))
    return segments

# def remove_noise(path, threshold):
#     # Load the audio file with pydub
#     audio = AudioSegment.from_file(path)

#     # Convert the audio to numpy array for faster processing
#     audio_data = audio.get_array_of_samples()
    
#     # Apply noise gating to reduce volume of segments below the threshold
#     for i in range(len(audio_data)):
#         if abs(audio_data[i]) < threshold:
#             audio_data[i] = 0

#     # Convert the modified array back to AudioSegment
#     processed_audio = audio._spawn(audio_data)
    
#     return processed_audio

# def remove_noise2(path):
#     # load audio
#     rate, data = wav.read(path)
#     # Remove noise from audio
#     reduced_noise = nr.reduce_noise(y= data, , verbose=True)
#     return reduced_noise