from setuptools import setup

setup(
  name = "vlog",
  version = "1.0.0",
  author = "John Baber-Lucero",
  author_email = "pypi@frundle.com",
  description = ("log functions with arbitrary verbosity"),
  license = "GPLv3",
  url = "https://github.com/jbaber/vlog",
  packages = ['vlog'],
  install_requires = [],
  entry_points = {
    'console_scripts': ['vlog=vlog.vlog:main'],
  }
)


