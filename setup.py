import os

from setuptools import setup, find_packages

setup(
  name='livevideo',
  version='0.1',
  description='livevideo',
  long_description=('livevideo'),
  url='http://github.com/liu-xiao-guo/livevideo',
  license='MIT',
  author='xiaoguo, liu',
  author_email='liu-xiao-guo@yahoo.com',
  packages=find_packages(exclude=['tests*']),
  include_package_data=True,
  entry_points = {
  'console_scripts': [
    'livevideo = video.stream:main'
  ]
  },
  package_data={
    'static': 'video/static/*',
    'templates': 'video/templates/*'},
  classifiers=[
    "Private :: Do Not Upload"
  ],
)
