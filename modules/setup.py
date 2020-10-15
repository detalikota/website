from setuptools import setup
setup (
    name='vsearch',
    version='1.0',
    description='My search tool',
    author='Magomed',
    author_email='detalikota@gmail.com',
    url='none',
    py_modules=['vsearch'],
)

#install with py -3 setup.py sdist
#and then py -3 -m pip install vsearch-1.0.tar.gz