# Audio file formats
# .mp3 (compressed)
# .flac (less compressed)
# .wav (uncompressed)

# Audio signal parameters
# - number of channels (1:mono or 2:stereo: audio is coming from 2 diffrents directions)
# - sample width  (number of bytes of each sample)
# - framerate/ sample_rate (number of samples per second 44 100Hz)
# - number of frames 
# - values of a frame in binary format

import wave

def infos(audio_path):
    obj= wave.open(audio_path,"rb")
    
    n_channels = obj.getnchannels()
    sample_width =  obj.getsampwidth()
    n_frames = obj.getnframes()
    frame_rate = obj.getframerate()
    t_audio = obj.getnframes() / obj.getframerate()
    params = obj.getparams()

    print("number of channels", n_channels) 
    print("sample width",sample_width)
    print("frame rate", frame_rate )
    print("number of frames", n_frames)
    print("params", params)
    print("time", t_audio)
    obj.close()
    return params
    
infos("audioProcessing/hello.wav")
# infos("uploads/6bece6e5-1081-4e8a-a5ff-a2fd13576434-byVC.wav")

def get_frames(audio):
    obj = wave.open(audio,"rb")
    return obj.readframes(-1)

# print(len(get_frames("uploads/6bece6e5-1081-4e8a-a5ff-a2fd13576434-byVC.wav")))


def get_copy(audio):
    f = wave.open(audio,"rb")
    nchannels = f.getnchannels()
    sample_width = f.getsampwidth()
    framerate = f.getframerate()
    frames = f.readframes(-1)
    filename = audio[:-4]
    f.close()

    new_filename = filename + "_NEW.wav"
    print(new_filename)
    nf = wave.open(new_filename, "wb")
    nf.setnchannels(nchannels)
    nf.setsampwidth(sample_width)
    nf.setframerate(framerate)
    nf.writeframes(frames)
    nf.close()
    print(" copied !!")

# get_copy("audioProcessing/hello.wav")