def create_duration_calculator(bpm: int = 120, beats_per_measure: int = 4, beat_note: int = 4):
    """
    Creates a function that calculates note durations for a given tempo and time signature.

    Arguments:
        bpm (int): Beats per minute.
        beats_per_measure (int): The top number of the time signature (e.g., 4 in 4/4 time).
        beat_note (int): The bottom number of the time signature, indicating which note gets one beat
                         (e.g., 4 for a quarter note, 8 for an eighth note).

    Returns:
        A function that takes a note value and returns its duration in seconds.
    """
    # 1. Calculate the duration of a single beat in seconds
    beat_duration_secs = 60.0 / bpm

    # 2. This is the function that will be returned
    def calculate(note_value: int):
        """
        Calculates the duration of a specific note type.

        Arguments:
            note_value (int): The type of note (1=whole, 2=half, 4=quarter, 8=eighth, etc.)

        Returns:
            The duration of the note in seconds (float).
        """
        # The duration is the beat duration multiplied by the note's value relative
        # to the note that gets the beat.
        multiplier = beat_note / note_value
        return beat_duration_secs * multiplier

    return calculate