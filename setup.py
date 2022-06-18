from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='utf8conv',
    version='0.0.2',
    description='conv files into utf-8 encoding',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='wangkuiju',
    author_email='kuijuwang@gmail.com',
    license='MIT License',
    install_requires=['chardet', 'tqdm'],
    packages=find_packages(),
    platforms=['all'],
    url='https://github.com/juju-w/utf8conv',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)