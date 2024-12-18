from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='cadmium-django-sdk',
    version='1.2.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.0.0',
        'Django>=3.0',
    ],
    description='Cadmium SDK for capturing and sending Django errors.',
    long_description=long_description,
    long_description_content_type='text/markdown',  
    author='bannawandoor',
    author_email='connect@hasanulbanna.in',
    url='https://github.com/bannawandoor27/cadmium-django-sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
)
