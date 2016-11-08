"""
Setup module.
"""
import re
from os.path import join as pjoin
from setuptools import setup


with open(pjoin('diapason', '__init__.py')) as f:
    line = next(l for l in f if l.startswith('__version__'))
    version = re.match('__version__ = [\'"]([^\'"]+)[\'"]', line).group(1)

setup(
    name='diapason',
    version=version,
    description='Python module to deal with note sounds.',
    long_description='''The diapason Python module can be used to deal with
        note sounds: WAV generation, note frequency calculation...''',
    url='https://github.com/Soundphy/diapason',
    author='Miguel Sánchez de León Peque',
    author_email='peque@neosit.es',
    license='License :: OSI Approved :: BSD License',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Education',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    keywords='diapason',
    packages=['diapason'],
    install_requires=['numpy', 'scipy'],
    extras_require={
        'dev': [],
        'test': ['tox'],
        'docs': ['sphinx', 'numpydoc', 'sphinx_rtd_theme'],
    },
)
