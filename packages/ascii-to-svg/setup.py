from setuptools import setup

setup(
    name='lektor-ascii-to-svg',
    version='0.1',
    author=',,,',
    author_email='',
    license='MIT',
    py_modules=['lektor_ascii_to_svg'],
    entry_points={
        'lektor.plugins': [
            'ascii-to-svg = lektor_ascii_to_svg:AsciiToSvgPlugin',
        ]
    }
)
