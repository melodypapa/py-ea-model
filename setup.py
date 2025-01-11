"""Minmal setup file for EA Assist"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read() 

setup(
    name='py_ea_model',
    version = '0.1.0',
    license = 'proprietary',
    description="The assistant tool for the Enterprise Architect",
    long_description=long_description,
    long_description_content_type="text/markdown",

    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='Enterprise Architect, UML, EA', 

    author = 'melodypapa',
    author_email = "melodypapa@outlook.com",
    url="https://github.com/melodypapa/py-ea-model",

    packages = find_packages(where='src'),
    package_dir= {'': 'src'},

    install_requires=['armodel', 'pywin32', 'openpyxl'],

    include_package_data=True,
    
    extras_require={'pytest': 'pytest-cov'},

    entry_points={
        'console_scripts': [
            'ea_test  = ea_model.cli.ea_test_cli:main',
        ]
    }
)