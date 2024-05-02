from setuptools import setup, find_packages
with open('README.md') as f:
    long_description = f.read()
setup(
    author='Princekumar Dobariya',
    author_email='princekumardobariya@gmail.com',
    description='A PyPI package for subsetsumdfs with a Markdown README',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name="subsetsumdfs",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[],
    entry_points = {
        "console_scripts" : [
            "subsetsumdfs = subsetsumdfs:subsetsum",
        ]
    }
)