from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name = "pygeoshapes",
  version = "1.0.0",
  description = "Use this package to draw some shapes by using Python",
  long_description = open('README.md').read(),
  url = '',
  author = "Mehrdad Kalateh Arabi",
  author_email = "mehrdad1234kalateh@gmail.com",
  License = "MIT",
  classifiers = classifiers,
  keywords = ['Butterfly', 'kite', 'Right_Angled_Triangle', 'Equilateral_Triangle', 'pygeoshapes'],
  packages = find_packages(),
  install_requires = ['']
)
