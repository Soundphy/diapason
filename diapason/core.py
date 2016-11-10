"""
Core diapason code.
"""
from io import BytesIO

from numpy import linspace, sin, pi, int16
from scipy.io import wavfile


def note_frequency(note, sharp=0, flat=0, octave=4, scientific=False):
    """
    Returns the frequency (in hertzs) associated to a given note.

    All the frequencies are based on the standard concert pitch or standard
    piano key frequencies, meaning that A4 (using scientific picth notation)
    is at 440 hertzs.

    Parameters
    ----------
    note : string
        Note to calculate the associated frequency from. Valid notes are
        characters from A to G.
    octave : int
        Octave position. Middle C and A440 being in the 4th octave.
    sharp : int
        Return a frequency higher in pitch by `sharp` semitones.
    flat : int
        Return a frequency lower in pitch by `flat` semitones.
    scientific : bool
        Use scientific pitch instead: C4 is set to 256 Hz.

    Returns
    -------
    float
        The frequency (in hertzs) associated to the given note.
    """
    if note not in list('ABCDEFG'):
        raise ValueError('Invalid note {}'.format(note))
    if sharp and flat:
        raise ValueError('Cannot set both sharp and flat parameters!')

    position = dict(C=0, D=2, E=4, F=5, G=7, A=9, B=11)
    if scientific:
        # C4 at 256 Hz
        base_note = 'C'
        base_octave = 4
        base_frequency = 256.
    else:
        # A4 at 440 Hz
        base_note = 'A'
        base_octave = 4
        base_frequency = 440.
    note_position = position[note] - position[base_note] + \
        (octave - base_octave) * 12
    note_position += sharp
    note_position -= flat
    frequency = 2 ** (note_position / 12.) * base_frequency

    return frequency


def generate_wav(frequency, duration, rate=44100):
    """
    Generate a WAV file reproducing a sound at a given frequency.

    Parameters
    ----------
    frequency : float
        Frequency, in hertzs, of the sound.
    duration : float
        Duration of the sound.
    rate : int
        Sample rate.

    Returns
    -------
    BytesIO
        The in-memory WAV file.
    """
    amplitude = 10000

    t = linspace(0, duration, duration * rate)
    data = sin(2 * pi * frequency * t) * amplitude
    data = data.astype(int16)

    note_io = BytesIO()
    wavfile.write(note_io, rate, data)

    return note_io
