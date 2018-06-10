from setuptools import setup

# Add markdown and string field with Jinja2 preprocessing.

setup(
    name='lektor-jinja2-fields',
    version='0.1',
    author=',,,',
    author_email='textshell@uchuujin.de',
    license='MIT',
    py_modules=['lektor_jinja2_fields'],
    entry_points={
        'lektor.plugins': [
            'jinja2-fields = lektor_jinja2_fields:Jinja2FieldsPlugin',
        ]
    }
)
