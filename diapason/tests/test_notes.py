"""
Test diapason notes.
"""
import pytest
from pytest import approx

from diapason import note_frequency


@pytest.mark.parametrize(('note', 'sharp', 'flat', 'octave', 'frequency'), [
    # Exact frequencies (A)
    ('A', 0, 0, 4, 440.),
    ('A', 0, 0, 0, 27.5),
    ('A', 0, 0, 6, 1760.),
    # Different notes in the same octave
    ('C', 0, 0, 4, 261.626),
    ('D', 0, 0, 4, 293.665),
    ('E', 0, 0, 4, 329.628),
    ('F', 0, 0, 4, 349.228),
    ('G', 0, 0, 4, 391.995),
    ('A', 0, 0, 4, 440.000),
    ('B', 0, 0, 4, 493.883),
    # Sharp
    ('C', 1, 0, 4, 277.183),
    ('D', 1, 0, 4, 311.127),
    ('E', 1, 0, 4, 349.228),
    ('F', 1, 0, 4, 369.994),
    ('G', 1, 0, 4, 415.305),
    ('A', 1, 0, 4, 466.164),
    ('B', 1, 0, 4, 523.251),
    # Flat
    ('C', 0, 1, 4, 246.942),
    ('D', 0, 1, 4, 277.183),
    ('E', 0, 1, 4, 311.127),
    ('F', 0, 1, 4, 329.628),
    ('G', 0, 1, 4, 369.994),
    ('A', 0, 1, 4, 415.305),
    ('B', 0, 1, 4, 466.164),
    # Double sharp
    ('C', 2, 0, 4, 293.665),
    ('D', 2, 0, 4, 329.628),
    ('E', 2, 0, 4, 369.994),
    ('F', 2, 0, 4, 391.995),
    ('G', 2, 0, 4, 440.000),
    ('A', 2, 0, 4, 493.883),
    ('B', 2, 0, 4, 554.365),
    # Double flat
    ('C', 0, 2, 4, 233.082),
    ('D', 0, 2, 4, 261.626),
    ('E', 0, 2, 4, 293.665),
    ('F', 0, 2, 4, 311.127),
    ('G', 0, 2, 4, 349.228),
    ('A', 0, 2, 4, 391.995),
    ('B', 0, 2, 4, 440.000),
    # Changing octave
    ('C', 0, 0, 5, 523.251),
    ('E', 1, 0, 7, 2793.83),
    ('C', 0, 0, 3, 130.813),
    ('E', 1, 0, 1, 43.6535),
])
def test_note_frequency(note, sharp, flat, octave, frequency):
    """
    Basic note_frequency() function tests.
    """
    actual = note_frequency(note, sharp=sharp, flat=flat, octave=octave)
    assert actual == approx(frequency, rel=1e-5)


@pytest.mark.parametrize(('note', 'sharp', 'flat', 'octave', 'frequency'), [
    # Exact frequencies (C)
    ('C', 0, 0, 0, 16.),
    ('C', 0, 0, 2, 64.),
    ('C', 0, 0, 4, 256.),
    ('C', 0, 0, 6, 1024.),
    ('C', 0, 0, 8, 4096.),
    # Other frequencies
    ('A', 0, 0, 4, 430.539),
])
def test_note_frequency_scientific(note, sharp, flat, octave, frequency):
    """
    Test note frequency calculation with scientific pitch.
    """
    actual = note_frequency(note, sharp=sharp, flat=flat, octave=octave,
                            scientific=True)
    assert actual == approx(frequency, rel=1e-5)


@pytest.mark.parametrize(('note', 'sharp', 'flat', 'octave'), [
    ('A', 1, 1, 4),
    ('Z', 0, 0, 4),
])
def test_note_frequency_value_errors(note, sharp, flat, octave):
    """
    Test note_frequency() ValueError exceptions.
    """
    with pytest.raises(ValueError):
        note_frequency(note, sharp, flat, octave)
