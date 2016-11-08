"""
Test file formats.
"""
import wave

import numpy
import pytest
from pytest import approx
from scipy.io import wavfile
from scipy.fftpack import fft

from diapason import generate_wav


@pytest.mark.parametrize(('frequency', 'duration', 'rate'), [
    (440., 2., 44100),
    (220., 1., 48000),
    (880., 3., 16000),
])
def test_generate_wav(frequency, duration, rate):
    """
    Test generated WAV files.
    """
    # Test using `wave`
    bytesio = generate_wav(frequency, duration, rate)
    wav = wave.open(bytesio)
    assert wav.getnchannels() == 1
    assert wav.getframerate() == rate
    assert wav.getnframes() / wav.getframerate() == approx(duration)

    # Test using `scipy`
    bytesio = generate_wav(frequency, duration, rate)
    scipyrate, data = wavfile.read(bytesio)
    assert scipyrate == rate
    assert len(data) / rate == approx(duration)
    transformed = fft(data)
    absolute = abs(transformed[:len(transformed) / 2 - 1])
    assert numpy.argmax(absolute) / duration == approx(frequency)
