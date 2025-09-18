import numpy as np

class Waveform():
    def __init__(self):
        '''
            Class constructor. general class for a waveform
        '''
        pass

    def transform(self, freq : float = 440.0, 
                 duration : float = 5.0, 
                 volume : float = 0.5, 
                 fs : int = 44100):
        return np.array([])

class Sine(Waveform):
    # class for a sine wave
    def __init__(self):
        super().__init__()
        pass

    def transform(self, freq : float = 440.0, 
                 duration : float = 5.0, 
                 volume : float = 0.5, 
                 fs : int = 44100):
        sample = (np.sin(2 * np.pi * np.arange(fs * duration) * freq / fs)).astype(np.float32)
        return sample
    
class Square(Waveform):
    # class for a square wave
    def __init__(self):
        super().__init__()
        pass

    def transform(self, freq : float = 440.0, 
                 duration : float = 5.0, 
                 volume : float = 0.5, 
                 fs : int = 44100):
        sample = np.sign(np.sin(2 * np.pi * np.arange(fs * duration) * freq / fs)).astype(np.float32)
        return sample

class Sawtooth(Waveform):
    # class for a sawtooth wave
    def __init__(self):
        super().__init__()
        pass

    def transform(self, freq : float = 440, 
                 duration : float = 5.0, 
                 volume : float = 0.5, 
                 fs : int = 44100):
        x = np.arange(fs * duration//2) * freq / fs
        sample = 2 * (x - np.floor(x + 0.5))
        return sample
    
# waveform transformers exported
sine_transformer = Sine()
square_transformer = Square()
sawtooth_transformer = Sawtooth()