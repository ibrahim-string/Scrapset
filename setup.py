from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Scrapset',
    version='1.4.0',
    description='DataScraper: Effortless Dataset Extraction',
    author='Ibrahim',
    author_email='string2025@gmail.com',
    packages=find_packages(),
    install_requires=[
        'selenium',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
)
