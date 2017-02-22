from setuptools import setup
def readme():
    with open('README.rst') as f:
        return f.read()
setup(name='copyusb',
      version='0.0.2',
      description='Copy connected USB media device to current script directory.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Filesystems',
      ],
      keywords='usb copy clone copier cloner drive',
      url='http://github.com/arsho/copyusb',
      author='Ahmedur Rahman Shovon',
      author_email='shovon.sylhet@gmail.com',
      license='MIT',
      packages=['copyusb'],
      include_package_data=True,
      zip_safe=False)
