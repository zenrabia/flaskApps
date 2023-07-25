from pydub import AudioSegment
import numpy as np

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

