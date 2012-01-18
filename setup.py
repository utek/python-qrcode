#!/usr/bin/env python
from distutils.core import setup

setup(
    name='qrcode',
<<<<<<< HEAD
    version='2.2',
    url='https://github.com/utek/python-qrcode',
    maintainer='utek',
    maintainer_email='mail@utek.pl',
    #download_url='',
    description='QR Code image generator',
    license='BSD',
    long_description=open('README.rst').read(),
    author='Lincoln Loop',
    author_email='info@lincolnloop.com',
    platforms=['any'],
    packages=[
        'qrcode',
        'qrcode.renderers'
    ],
    scripts=[
        'scripts/qr',
    ],
    package_data={'': ['LICENSE']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
