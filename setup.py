try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': """
This is a baasic program for entry into Code Fellows: Python 401 course.
It will generate a school with class rooms which will have classes.
Each class will have a teacher and students having no more than 10 students \
per teacher.
""",
    'author': 'Chris Hudson',
    'url': 'https://github.com/CaHudson94/CFEntryTest',
    'download_url': 'https://github.com/CaHudson94/CFEntryTest',
    'author_email': 'c.ahudson84@yahoo.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['CFEntryTest'],
    'scripts': [],
    'name': 'Code Fellows Entry Test'
}

setup(**config)
