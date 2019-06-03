import os
from setuptools import setup


def read(fname):
    """Helper to read README"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()


setup(
      name='bind',
      version='2.1.0',  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT
      description='A function for binding strings with a separator',
      author='Bitpanda GmbH',
      author_email='nosupport@bitpanda.com',
      url='https://github.com/bitpanda-labs/bind',
      packages=['bind'],
      package_data={'bind': ['py.typed']},
      zip_safe=False,  # For mypy to be able to find the installed package
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      python_requires='>=3.6',
)
