from setuptools import setup, find_packages

setup(
    name='ek_data_structures',
    version="0.0.1",
    description='A Python package that implements common data structures such as Array, Stack, Queue, Linked List, Binary Tree, and Graph.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Emmanuel Kirui Barkacha',
    author_email='ebarkacha@aimsammi.org',
    url='https://github.com/ekbarkacha/data-structure-package',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
