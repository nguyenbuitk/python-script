try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'My project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.2',
    'install_requires': ['nose'],
    'packages': ['gothonweb'],
    'scripts': [],
    'name': 'projectGothon'
}
setup(**config)