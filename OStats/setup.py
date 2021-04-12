from setuptools import setup, find_packages

setup(name = 'ostats',
      version = '0.1',
      description = 'Basic statistics functions and plotting',
      url = 'https://github.com/OClarkson/OStats',
      author = 'Ondrea Clarkson',
      author_email = 'ondreaclarkson@gmail.com',
      license = 'MIT',
      packages = find_packages(),
      zip_safe = False, install_requires=['numpy', 'pandas', 'matplotlib'])