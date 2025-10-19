import numpy as np
def overlay_tracks(*tracks : bytes) -> bytes:
    '''
        Overlays multiple tracks (list of waveform bytestrings) into a single track.
    '''
    # pre-setup check
    if not isinstance(tracks, tuple) or len(tracks) < 2:
        raise ValueError("At least two tracks must be provided as a list of bytestrings")
    
    # setup
    track_arrays = []
    max_length = 0
    # for track in tracks:
    for track in tracks:
        if not isinstance(track, bytes):
            raise ValueError("Each track must be of type `bytes`")
        track_array = np.frombuffer(track, dtype=np.float32)
        track_arrays.append(track_array)
        if len(track_array) > max_length:
            max_length = len(track_array)

    # pad tracks to the same length and then add to an empty array
    mixed_track = np.zeros(max_length, dtype=np.float32)
    for track_array in track_arrays:
        if len(track_array) < max_length:
            track_array = np.pad(track_array, (0, max_length - len(track_array)))
        mixed_track += track_array

    # normalize the mixed track to prevent clipping
    max_amplitude = np.max(np.abs(mixed_track))
    if max_amplitude > 1.0:
        mixed_track = mixed_track / max_amplitude
    
    return mixed_track.tobytes()  # placeholder implementation
