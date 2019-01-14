import re

from setuptools import setup


version = ''
with open('diskspace/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)


if not version:
    raise RuntimeError('version is not set')


setup(
    name='diskspace',
    author='AlexFlipnote',
    url='https://github.com/AlexFlipnote/DiskSpace',
    version=version,
    packages=['diskspace'],
    license='GNU v3',
    description='Making it possible to use Linux df & du command on Windows',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'diskspace=diskspace.diskspace:main',
            'ds=diskspace.diskspace:main'
        ]
    }
)
