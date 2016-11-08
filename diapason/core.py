"""
Core diapason code.
"""
from io import BytesIO

from numpy import linspace, sin, pi, int16
from scipy.io import wavfile


def note_frequency(note, sharp=0, flat=0, octave=4):
    """
    Returns the frequency (in hertzs) associated to a given note.

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
    note_number = octave * 12 + position[note] + 1
    note_number += sharp
    note_number -= flat
    frequency = 2 ** ((note_number - 58) / 12.) * 440.

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
