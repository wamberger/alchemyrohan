

from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="alchemyrohan",
    version="1.0.0",
    author="Alan Wamberger",
    author_email="alanwamberger@protonmail.com",
    description="Package to auto-create SqlAlchemy model in Python code itself",
    long_description=long_description,
    url="https://wamberger.eu",
    packages=find_packages(),
    install_requires='sqlalchemy',
    python_requires='>=3.11.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)