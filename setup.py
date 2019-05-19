# https://stackoverflow.com/a/50468400
from setuptools import setup

setup (
    name='toggle-refresh',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'toggle-refresh=update_display:run'
        ]
    }
)
