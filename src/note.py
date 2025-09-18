from .waveform import *


class Note():

    def __init__(self, freq : float = 440.0, 
                 duration : float = 5.0, 
                 volume : float = 0.5, 
                 fs : int = 44100):
        '''
            Class constructor.
            Arguments:
                `freq` : float, optional
                    Note frequency
                `volume` : float, optional
                    Volume in decibels
                `duration` : float, optional
                    Duration in seconds
                `fs` : int, optional
                    Sampling rate
        '''
        # some tests to ensure that the values are within type constraints
        if not isinstance(fs, int):
            raise ValueError("Sampling rate must be an integer")
        if not isinstance(freq, float) and not isinstance(freq, int):
            raise ValueError("Frequency must be a number")
        if not isinstance(volume, float) and not isinstance(volume, int):
            raise ValueError("Volume must be a number")
        if not isinstance(duration, float) and not isinstance(duration, int):
            raise ValueError("Duration must be a number")
        
        if volume > 1 or volume < 0:
            raise ValueError("Volume must be between 0 and 1")
        if duration < 0:
            raise ValueError("Duration must be a positive number")
        if fs < 0:
            raise ValueError("Sampling rate must be a positive number")
        if freq < 0:
            raise ValueError("Frequency must be a positive number")
        
        # proceeding to init if okay
        self.freq = freq
        self.volume = volume
        self.duration = duration
        self.fs = fs

    def fit(self, transformer : Waveform = Sine()):
        # just a check to see if the transformer is an instance of Waveform class
        if not isinstance(transformer, Waveform):
            raise ValueError("Transformer must be an instance of Waveform class")
        # play the note
        
        # play the note with a Sine wave
        sample = transformer.transform(self.freq, self.duration, self.volume, self.fs)
        return sample.tobytes()
    
