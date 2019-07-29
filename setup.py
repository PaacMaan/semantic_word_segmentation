from setuptools import setup

setup(name='fr_word_segment',
      version='0.1',
      description='A package that split mispelled words semantically',
      url='https://github.com/PaacMaan/semantic-word-segmentation',
      author='Ayoub RMIDI',
      author_email='ayoub.rmidi@gmail.com',
      license='MIT',
      packages=['fr_word_segment'],
      install_requires=[
          'spacy',
      ],
      zip_safe=False)