import setuptools

from packagename.version import Version

setuptools.setup(
  name='scrubby',
  version=Version('0.1.0').number,
  description='Scrubby CLI.',
  long_description=open('README.md').read().strip(),
  author='Robin Orheden',
  author_email=None,
  url='https://github.com/typerandom/scrubby/',
  py_modules=['scrubby'],
  install_requires=[],
  license='MIT License',
  zip_safe=False,
  keywords='database scrubbing',
  classifiers=['Data', 'Scrubbing'],
)