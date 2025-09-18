import pyaudio

def play(fs : int = 44100, audio_sample : bytes = b'', n_channels : int = 1):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=n_channels,
                    rate= fs,
                    output=True)
    stream.write(audio_sample)
    stream.stop_stream()
    stream.close()
    p.terminate()