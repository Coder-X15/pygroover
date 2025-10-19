import pytest
import unittest
import sys
import os

# Get the absolute path to the project root (the parent of the test folder)
SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# insert this path in sys path
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

import src.note as pgn  # type: ignore
import src.mixer as pgm  # type: ignore
import src.beat as pgb  # type: ignore
from src.globals import notes_freq_dict  # type: ignore
import src.waveform as pgwf  # type: ignore

# requirements to test
# 1. input must be tuple of bytes objects
# abilities to test:
# 1. handle unequal length tracks
class TrackOverlayTest(unittest.TestCase):

    def setUp(self) -> None:
        self.note_duration = pgb.create_duration_calculator(bpm=120, beats_per_measure=4, beat_note=1)
        self.track1 = [
            ('C4', self.note_duration(4)),
            ('D4', self.note_duration(4)),
            ('F4', self.note_duration(4)),
            ('D4', self.note_duration(4)),
            ('A4', self.note_duration(4)),
            ('mute', self.note_duration(2)),
            ('A4', self.note_duration(4)),
            ('mute', self.note_duration(2)),
            ('G4', self.note_duration(2)),
            ('mute', self.note_duration(1)),
            ('C4', self.note_duration(4)),
            ('D4', self.note_duration(4)),
            ('F4', self.note_duration(4)),
            ('D4', self.note_duration(4)),
            ('G4', self.note_duration(4)),
            ('mute', self.note_duration(2)),
            ('G4', self.note_duration(4)),
            ('mute', self.note_duration(2)),
            ('F4', self.note_duration(2)),
            ('E4', self.note_duration(4)),
            ('D4', self.note_duration(2)),
            ('mute', self.note_duration(2)),
            ('C4', self.note_duration(4)),
            ('D4', self.note_duration(4)),
            ('F4', self.note_duration(4)),
            ('D4', self.note_duration(4)),
            ('F4', self.note_duration(1)),
            ('G4', self.note_duration(2)),
            ('E4', self.note_duration(1)),
            ('D4', self.note_duration(4)),
            ('C4', self.note_duration(4)),
            ('mute', self.note_duration(2)),
            ('C4', self.note_duration(2)),
            ('G4', self.note_duration(2)),
            ('mute', self.note_duration(2)),
            ('F4', self.note_duration(2)),
            ('mute', self.note_duration(4))
        ]

        notes2 = [
            ('mute', self.note_duration(1)),
            ('F4', self.note_duration(1)),
            ('mute', self.note_duration(2)),
            ('G4', self.note_duration(1)),
            ('mute', self.note_duration(2)),
            ('C4', self.note_duration(2)),
            ('mute', self.note_duration(2)),
            ('G4', self.note_duration(1)),
            ('mute', self.note_duration(2)),
            ('A4', self.note_duration(1)),
            ('mute', self.note_duration(2)),
            ('C5', self.note_duration(4)),
            ('B4', self.note_duration(4)),
            ('A4', self.note_duration(4)),
            ('G4', self.note_duration(4)),
            ('F4', self.note_duration(1)),
            ('mute', self.note_duration(2)),
            ('G4', self.note_duration(1)),
            ('mute', self.note_duration(2)),
            ('C4', self.note_duration(1)),
            ('mute', self.note_duration(4)),
            ('C4', self.note_duration(1)),
            ('mute', self.note_duration(4))
        ]
        self.note_bytes1 = []
        self.note_bytes2 = []
        for note, duration in self.track1:
            self.note_bytes1.append(pgn.Note(freq = notes_freq_dict[note], duration = duration, volume = 0.5).fit(pgwf.square_transformer))

        for note, duration in notes2:
            self.note_bytes2.append(pgn.Note(freq = notes_freq_dict[note], duration = duration, volume = 0.2).fit(pgwf.sine_transformer))

        self.note_bytes1 = b''.join(self.note_bytes1)
        self.note_bytes2 = b''.join(self.note_bytes2)
        return super().setUp()
    
    def test_input_type_string(self):
        # testing whether an exception occurs if input is string
        with self.assertRaises(ValueError):
            pgm.overlay_tracks("not a list", self.note_bytes2) # type: ignore

    def test_input_type_int(self):
        # testing whether an exception occurs if input is int   
        # testing if elements are np.ndarray
        with self.assertRaises(ValueError):
            pgm.overlay_tracks(12345, self.note_bytes2) # type: ignore

    def test_input_type_list(self):
        # testing whether an exception occurs if input is list
        with self.assertRaises(ValueError):
            pgm.overlay_tracks(self.note_bytes1, [12345, "hahah"]) # type: ignore

    def test_input_type_float(self):
        # testing whether an exception occurs if input is float
        with self.assertRaises(ValueError):
            pgm.overlay_tracks(12.34, self.note_bytes2) # type: ignore
    
    def test_overlay_different_lengths(self):
        # testing overlaying two notes of different lengths
        try:
            mixed_track = pgm.overlay_tracks(self.note_bytes1, self.note_bytes2) # type: ignore
        except Exception as e:
            self.fail(f"Overlaying tracks of different lengths raised an exception: {e}")

if __name__ == "__main__":
    pytest.main(args=["-vv"])