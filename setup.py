from setuptools import setup

from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='signer_icpedu',
    version='0.0.1',
    license='MIT License',
    author='Kemuel Rocha',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='kemuelsr@gmail.com',
    keywords='signer icpedu',
    description=u'Package para assinaturas digitais',
    packages=['signer_icpedu'],
    install_requires=[r.strip() for r in open('requirements.txt').read().splitlines()])