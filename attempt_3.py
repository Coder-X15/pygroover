# overlay test

from src.note import *
from src.beat import *
from src.player import *
from src.waveform import *
from src.globals import *

note_duration = create_duration_calculator(bpm=120, beats_per_measure=4, beat_note=1)

notes1 = [
    ('C4', note_duration(4)),
    ('D4', note_duration(4)),
    ('F4', note_duration(4)),
    ('D4', note_duration(4)),
    ('A4', note_duration(4)),
    ('mute', note_duration(2)),
    ('A4', note_duration(4)),
    ('mute', note_duration(2)),
    ('G4', note_duration(2)),
    ('mute', note_duration(1)),
    ('C4', note_duration(4)),
    ('D4', note_duration(4)),
    ('F4', note_duration(4)),
    ('D4', note_duration(4)),
    ('G4', note_duration(4)),
    ('mute', note_duration(2)),
    ('G4', note_duration(4)),
    ('mute', note_duration(2)),
    ('F4', note_duration(2)),
    ('E4', note_duration(4)),
    ('D4', note_duration(2)),
    ('mute', note_duration(2)),
    ('C4', note_duration(4)),
    ('D4', note_duration(4)),
    ('F4', note_duration(4)),
    ('D4', note_duration(4)),
    ('F4', note_duration(1)),
    ('G4', note_duration(2)),
    ('E4', note_duration(1)),
    ('D4', note_duration(4)),
    ('C4', note_duration(4)),
    ('mute', note_duration(2)),
    ('C4', note_duration(2)),
    ('G4', note_duration(2)),
    ('mute', note_duration(2)),
    ('F4', note_duration(2)),
    ('mute', note_duration(4))
]

notes2 = [
    ('mute', note_duration(1)),
    ('F4', note_duration(1)),
    ('mute', note_duration(2)),
    ('G4', note_duration(1)),
    ('mute', note_duration(2)),
    ('C4', note_duration(2)),
    ('mute', note_duration(2)),
    ('G4', note_duration(1)),
    ('mute', note_duration(2)),
    ('A4', note_duration(1)),
    ('mute', note_duration(2)),
    ('C5', note_duration(4)),
    ('B4', note_duration(4)),
    ('A4', note_duration(4)),
    ('G4', note_duration(4)),
    ('F4', note_duration(1)),
    ('mute', note_duration(2)),
    ('G4', note_duration(1)),
    ('mute', note_duration(2)),
    ('C4', note_duration(1)),
    ('mute', note_duration(4)),
    ('C4', note_duration(1)),
    ('mute', note_duration(4))
]

# convert each of them into the note samples
note_bytes1 = []
note_bytes2 = []

for note, duration in notes1:
    note_bytes1.append(Note(freq = notes_freq_dict[note], duration = duration, volume = 0.5).fit(square_transformer))

for note, duration in notes2:
    note_bytes2.append(Note(freq = notes_freq_dict[note], duration = duration, volume = 0.2).fit(sine_transformer))




# concat the bytes
concated_song1 = b''.join(note_bytes1)
concated_song2 = b''.join(note_bytes2)

blyat1 = np.frombuffer(concated_song1, dtype=np.float32)
blyat2 = np.frombuffer(concated_song2, dtype=np.float32)

# fix size issues before vstack
if len(blyat1) > len(blyat2):
    blyat2 = np.pad(blyat2, (0, len(blyat1) - len(blyat2)))
elif len(blyat2) > len(blyat1):
    blyat1 = np.pad(blyat1, (0, len(blyat2) - len(blyat1)))


# overlay blyat2 on blyat1
final = (blyat1 + blyat2)/2
# final = blyat2
song = final.tobytes()

# play the song
play(audio_sample = song, n_channels=1)
