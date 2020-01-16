from distutils.core import setup
setup(
  name = 'SeleniumCookie',
  packages = ['SeleniumCookie'],
  version = '0.1',
  license='MIT',
  description = 'COOKIE INJECTION FOR SELENIUM',
  author = 'THANKSTOALL',
  author_email = 'pchackers18@gmail.com',
  url = 'https://github.com/D-E-F-E-A-T/Selenium-Cookie-Injector',
  download_url = 'https://github.com/D-E-F-E-A-T/Selenium-Cookie-Injector/archive/v_01.tar.gz',
  keywords = ['SELENIUM', 'COOKIE'],
  install_requires=[
		'pyaes','pbkdf2','keyring','lz4', 'configparser'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',  
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
