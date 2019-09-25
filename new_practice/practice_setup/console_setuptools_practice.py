from distutils.core import setup


setup(name="rebuildd",
      description="Debian packages rebuild tool",
      author="Pavel Malin",
      author_email="kurchevskijpavel@gmail.com",
      url="https://github.com/pavel-malin",
      entry_points={
          'console_scripts': [
              'rebuildd = rebuilld:main',
          ]
      },
      packages=['rebuildd'])
