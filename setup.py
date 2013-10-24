from setuptools import setup
from pip.req import parse_requirements

# workaround a broken pip
class Options(object): pass
opts = Options(); opts.skip_requirements_regex = None
#

requires = [str(ir.req) for ir in
            parse_requirements('requirements.txt', options=opts)]

setup(
    name='mkzone',
    version="0.0.1",
    description = 'generates bind zone files from yaml',
    author = 'Mike Sampson',
    author_email = 'mfs',
    license = 'GPLv3',
    long_description = 'generates bind zone files from yaml',
    packages = ['mkzone'],
    install_requires = requires,
    entry_points = {'console_scripts': ['mkzone = mkzone:main']},
)
