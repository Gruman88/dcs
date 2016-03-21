from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pydcs",
    version='0.8.2',
    description="A Digital Combat Simulator mission builder framework",
    long_description=long_description,
    url='https://github.com/pydcs/dcs',
    author="Peinthor Rene",
    author_email="peinthor@gmail.com",
    license="LGPLv3",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Games/Entertainment :: Simulation',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='dcs digital combat simulator eagle dynamics mission framework',
    packages=['dcs', 'dcs/terrain', 'dcs/lua'],
    entry_points={
        'console_scripts': [
            'dcs_random=dcs.random_mission:main'
        ]
    }
)
