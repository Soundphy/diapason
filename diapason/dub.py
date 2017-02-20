"""
Dub module that can be used when ffmpeg is available to deal with different
audio formats.
"""
from io import BytesIO

from pydub import AudioSegment


def convert_wav(wav, coding_format='mpeg', **kwargs):
    """
    Convert a WAV file to other formats.
    """
    assert coding_format in ('mpeg', 'vorbis')
    if coding_format == 'mpeg':
        coding_format = 'mp3'
    if coding_format == 'vorbis':
        coding_format = 'ogg'
    bitrate = kwargs.get('bitrate', None)
    converted = BytesIO()
    audio = AudioSegment.from_wav(wav)
    audio.export(converted, format=coding_format, bitrate=bitrate)
    return converted
