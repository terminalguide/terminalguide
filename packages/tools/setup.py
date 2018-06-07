from setuptools import setup

setup(
    name='lektor-tools',
    version='0.1',
    author='Martin Hostettler',
    author_email='',
    license='MIT',
    py_modules=['lektor_tools'],
    entry_points={
        'lektor.plugins': [
            'tools = lektor_tools:ToolsPlugin',
        ]
    }
)
