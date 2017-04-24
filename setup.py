from setuptools import find_packages, setup


setup_args = dict(
    name='gae-ranklist',
    version='1.0',
    maintainer='Thrust Interactive',
    packages=find_packages(),
)


if __name__ == '__main__':
    setup(**setup_args)
