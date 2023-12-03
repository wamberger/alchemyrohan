

from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_desc = f.read()


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    row = (l.strip() for l in open(filename))
    return [r for r in row if r and not r.startswith("#")]


setup(
    name="alchemyrohan",
    version="1.0.0",
    author="Alan Wamberger",
    author_email="alanwamberger@protonmail.com",
    description="Package to auto-create SqlAlchemy model in Python code itself",
    long_description=long_descr,
    url="https://wamberger.eu",
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    python_requires='>=3.10.0',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)