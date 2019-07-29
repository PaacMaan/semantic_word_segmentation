import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="fr_word_segment",
    version="0.1.0",
    description="A package that split mispelled words semantically",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/PaacMaan/semantic_word_segmentation.git",
    author="Ayoub RMIDI",
    author_email="ayoub.rmidi@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["fr_word_segment"],
    include_package_data=True,
    install_requires=["spacy"],
)