import matplotlib.pyplot as plt
import numpy as np
import wave

def plot_waveform(wave_file):
    with wave.open(wave_file, 'rb') as wf:
        num_channels = wf.getnchannels()
        sample_width = wf.getsampwidth()
        frame_rate = wf.getframerate()
        num_frames = wf.getnframes()

        # Read all frames
        frames = wf.readframes(num_frames)

        # Convert the binary data to a numpy array
        if sample_width == 1:
            dtype = np.uint8
        elif sample_width == 2:
            dtype = np.int16
        else:
            raise ValueError("Unsupported sample width")

        audio_data = np.frombuffer(frames, dtype=dtype)

    # Calculate the time values for each sample
    time_values = np.linspace(0, num_frames / frame_rate, num=num_frames)

    # Plot the waveform
    plt.figure(figsize=(10, 4))
    if num_channels == 2:
        plt.plot(time_values, audio_data[::2], label='Left Channel')
        plt.plot(time_values, audio_data[1::2], label='Right Channel')
    else:
        plt.plot(time_values, audio_data)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Waveform Plot')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    wav_file_path = "uploads/6bece6e5-1081-4e8a-a5ff-a2fd13576434-byVC.wav"
    plot_waveform(wav_file_path)
