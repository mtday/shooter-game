from setuptools import setup, find_packages

with open('README.md') as f:
    readme_file = f.read()

setup(
    name='shooter-game',
    version='0.0.0',
    description='Shooter Game',
    long_description=readme_file,
    url='https://github.com/mtday/shooter-game',
    install_requires=['pygame'],
    packages=find_packages(exclude=('tests', 'docs'))
)
