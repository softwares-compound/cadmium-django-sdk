from setuptools import setup, find_packages

setup(
    name='cadmium-django-sdk',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.0.0',
        'Django>=3.0',
    ],
    description='Cadmium SDK for capturing and sending Django errors.',
    author='Your Name',
    author_email='your_email@example.com',
    url='https://github.com/yourusername/cadmium-django-sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
)
