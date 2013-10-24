from setuptools import setup

setup(
    name='mkzone',
    version="0.0.1",
    description = 'generates bind zone files from yaml',
    author = 'Mike Sampson',
    author_email = 'mfs',
    license = 'GPLv3',
    long_description = 'generates bind zone files from yaml',
    packages = ['mkzone'],
    entry_points = {'console_scripts': ['mkzone = mkzone:main']},
)
