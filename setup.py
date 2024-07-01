from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='Task1',
    version='1.0',
    author='Fyodorov Nikita',
    author_email='fyodorov-nikita@inbox.ru',
    packages=find_packages(),
    install_requires=['django==2.2.2', 'm3-django-compat==1.9.2', 'm3-objectpack==2.2.47'],
)
