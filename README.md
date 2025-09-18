# PyGroover : Make Groovy Music in Python!

## Sections:
1. [Introduction](#intorduction)
2. [How To Use](#how-to-use)
3. [Upcoming Features](#upcoming-features)
4. [TODO](#todo)

## Intorduction
My main source of inspiration for this small project came from Strudel REPL. The very fact hat you can code music, with the backing from a Python module I used to work with (I forgot its name but it's something like `midi` according to my faint memory of it) drove me to work on this one whole day (didn't work hard since I had other stuff to do too, but it was on 17 September, 2025).

## How To Use
These steps work only in the current build. These shall be replaced with standard Python installation procedures once this becomes a Python module available on PyPI.
- Clone this repo and `cd` into it
- Create a `virtualenv` and activate it in the folder
- Install requirements: `pip install -r requirements.txt`
- Follow the syntax and make music, or run `python test2.py` for a groovy track to dance to.

## Syntax:
These work only in the current build. These shall be replaced with proper import replacements and whatever has to be used once this becomes a Python module available on PyPI.
- Imports:
    ```python
    from src.note import *
    from src.beat import *
    from src.player import *
    from src.waveform import *
    from src.globals import *
    ```
- Duration measurement instantiation:
    ```python
    note_duration = create_duration_calculator(bpm=<desired bpm>, 
                                                beats_per_measure=<desired beats per measure>, 
                                                beat_note=<which note gets a whole beat>)
    ```
    Now, the arguments `beats_per_measure` and `beat_note` are what determines the time signature of the song. The time signature will be $` \frac{\text{Beats per measure}}{\text{Beat note}} `$. Beat note can be something like $1$ (a whole note gets a beat), $2$ (a half note gets a beat), $4$ (a quarter note gets a beat) and so on. \
    With this, the duration of a note can be mentioned like:
    ```python
    note_duration(4) # a quarter note
    note_duration(2) # a half note
    note_duration(1) # a whole note
    ```
- Note instantiation:
    ```python
    A = Note() # the Note object, in its default settings, represent the reference note A @ 440Hz and with a volume of 0.5 decibels

    # the note A at volume of 0.5dB and a sampling rate of 44100 played for a duration of 1sec
    A = Note(freq = 440, volume = 0.5, fs = 44100, duration = 1)
    ```
    To change the note durations according to the note being played, one can use the `note_duration` function already created:
    ```python
    # a whole note A (the note duration is being measured according to the previous point's example)
    A = Note(freq = 440, volume = 0.5, fs = 44100, duration = note_duration(1))
    ```
    To get the corresponding waveform to play, one has to 'fit' the wave onto the waveform desired, like:
    ```python
    note_bytes = A.fit(sine_transformer) # a sine wave of the note A
    ```
    Mainly 3 wave transformers are available: `sine_transformer`, `square_transformer` and `sawtooth_transformer` (ref:`src/waveform.py`).
    **NB:** One can concatenate a collection of these notes at various durations (Also with rests, provided by the `mute` key of the `notes_freq_dict` global dictionary in `src/globals.py`) by appending the fitted waveforms:
    ```python
    notes = [
    ('C4', note_duration(4)),
    ('D4', note_duration(4)),
    ('F4', note_duration(4)),
    ('D4', note_duration(4)),
    ('A4', note_duration(4)),
    ('mute', note_duration(2))]

    # convert each of them into the note samples
    note_bytes = []

    for note, duration in notes:
        note_bytes.append(Note(freq = notes_freq_dict[note], duration = duration).fit(sawtooth_transformer))

    # concat the bytes
    concated_song = b''.join(note_bytes)
    ```
- Playing the created track:
    ```python
    # play the song
    play(audio_sample = concated_song)
    ```
    Ref: `src/player.py`

## Upcoming Features
These may arrive either via collaboration or by myself, my involvement may reduce as of now though. It will be great to have great collaborators from the community!
1. Sound mixing
2. More waveform transformers
3. Drum synths
4. Track looping
5. Grammar for interpreting note strings (inputs like `"A42 B42 C#44 - C#42"` etc.)
In short, one will be able to use PyGroover just like Strudel REPL but without the live component for now (until another ambitious warrior makes it happen!!).

## TODO
Phase 1:
1. Write unit tests
2. Implement more wave transformers if I can/ I have time
    - Triangle (done)
    - Any other stuff I don't really know about
3. Add a `setup.py` file if I can, plus some path fixing ig????
4. Add MIDI sounds (classic piano, guitar)


    
