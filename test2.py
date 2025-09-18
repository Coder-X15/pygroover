from src.note import *
from src.beat import *
from src.player import *
from src.waveform import *
from src.globals import *

note_duration = create_duration_calculator(bpm=120, beats_per_measure=4, beat_note=1)

# putting the notes for an amazing track
notes = [
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
    ('F4', note_duration(4))
]

# convert each of them into the note samples
note_bytes = []

for note, duration in notes:
    note_bytes.append(Note(freq = notes_freq_dict[note], duration = duration).fit(square_transformer))

# concat the bytes
concated_song = b''.join(note_bytes)

# play the song
play(audio_sample = concated_song)