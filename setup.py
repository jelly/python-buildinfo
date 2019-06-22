import os

from setuptools import setup

setup(
    name='buildinfo',
    version='0.0.1',
    packages=['buildinfo'],

    description=('A small library to parse .BUILDINFO files'),
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url='https://github.com/jelly/python-buildinfo',
    license='MIT',

    author='Jelle van der Waa',
    author_email='jelle@vdwaa.nl',

    install_requires=['parse'],

    entry_points={
        'console_scripts': [
            'parse_buildinfo = buildinfo.main:main',
        ]
    },

    keywords='.BUILDINFO pacman',

    classifiers=[
        "Development Status :: 3 - Alpha",
        'Topic :: System :: Archiving :: Packaging',
        'License :: OSI Approved :: MIT License (MIT)',
    ],
)
