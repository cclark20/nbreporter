from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

long_description = 'Package to generate notebooks and other \
    output formats based off a notebook template.'

setup(
    name = 'nbtemplate',
    version = '1.0.0',
    author = 'Casey Clark',
    author_email = 'caseyclark0123@gmail.com',
    url = 'https://github.com/cclark20/nbtemplate',
    description = 'Notebook template runner.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    license = 'MIT',
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'nbtemplate = nbtemplate.nbtemplate:main'
        ]
    },
    classifiers = (
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ),
    install_requires = requirements,
    zip_safe = False
)