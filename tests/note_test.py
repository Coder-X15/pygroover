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

class WaveformTest(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def test_frequency_string(self):
        # testing for sine waveform transformer
        with self.assertRaises(ValueError):
            pgn.Note(
                freq = "440", # type: ignore
                duration = 5.0,
                volume = 0.5,
                fs = 44100
            )

            pgn.Note(
                freq = "440.00", # type: ignore
                duration = 5.0,
                volume = 0.5,
                fs = 44100
            )

    def test_frequency_none(self):
        # testing for sine waveform transformer
        with self.assertRaises(ValueError):
            pgn.Note(
                freq = None, # type: ignore
                duration = 5.0,
                volume = 0.5,
                fs = 44100
            )

    def test_frequency_negative(self):
        # testing for sine waveform transformer
        with self.assertRaises(ValueError):
            pgn.Note(
                freq = -440.0,
                duration = 5.0,
                volume = 0.5,
                fs = 44100
            )

    def test_sampling_rate_string(self):
        # testing for sine waveform transformer
        with self.assertRaises(ValueError):
            pgn.Note(
                freq = 440.0,
                duration = 5.0,
                volume = 0.5,
                fs = "44100" # type: ignore
            )

            pgn.Note(
                freq = 440.0,
                duration = 5.0,
                volume = 0.5,
                fs = "44100.00" # type: ignore
            )

    def test_sampling_rate_none(self):
        # testing for sine waveform transformer
        with self.assertRaises(ValueError):
            pgn.Note(
                freq = 440.0,
                duration = 5.0,
                volume = 0.5,
                fs = None # type: ignore
            )

    def test_sampling_rate_negative(self):
        # testing for sine waveform transformer
        with self.assertRaises(ValueError):
            pgn.Note(
                freq = 440.0,
                duration = 5.0,
                volume = 0.5,
                fs = -44100
            )

    def test_volume_string(self):
        # testing for sine waveform transformer
        with self.assertRaises(ValueError):
            pgn.Note(
                freq = 440.0,
                duration = 5.0,
                volume = "0.5", # type: ignore
                fs = 44100
            )

            pgn.Note(
                freq = 440.0,
                duration = 5.0,
                volume = "0.50", # type: ignore
                fs = 44100
            )

    def test_volume_none(self):
        # testing for sine waveform transformer
        with self.assertRaises(ValueError):
            pgn.Note(
                freq = 440.0,
                duration = 5.0,
                volume = None, # type: ignore
                fs = 44100
            )

    def test_volume_out_of_bounds(self):
        # testing for sine waveform transformer
        with self.assertRaises(ValueError):
            pgn.Note(
                freq = 440.0,
                duration = 5.0,
                volume = 1.5,
                fs = 44100
            )

            pgn.Note(
                freq = 440.0,
                duration = 5.0,
                volume = -0.5,
                fs = 44100
            )

    def test_duration_string(self):
        # testing for sine waveform transformer
        with self.assertRaises(ValueError):
            pgn.Note(
                freq = 440.0,
                duration = "5.0", # type: ignore
                volume = 0.5,
                fs = 44100
            )

            pgn.Note(
                freq = 440.0,
                duration = "5", # type: ignore
                volume = 0.5,
                fs = 44100
            )

    def test_duration_none(self):
        # testing for sine waveform transformer
        with self.assertRaises(ValueError):
            pgn.Note(
                freq = 440.0,
                duration = None, # type: ignore
                volume = 0.5,
                fs = 44100
            )
    
    def test_duration_negative(self):
        # testing for sine waveform transformer
        with self.assertRaises(ValueError):
            pgn.Note(
                freq = 440.0,
                duration = -5.0,
                volume = 0.5,
                fs = 44100
            )

if __name__ == "__main__":
    pytest.main(args=["-vv"])