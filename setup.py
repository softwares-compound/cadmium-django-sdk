from setuptools import setup, find_packages

setup(
    name='cadmium-django-sdk',
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.0.0',
        'Django>=3.0',
    ],
    description='Cadmium SDK for capturing and sending Django errors.',
    author='bannawandoor',
    author_email='connect@hasanulbanna.in',
    url='https://github.com/bannawandoor27/cadmium-django-sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
)
