import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Escrapper",
    version="0.0.1",
    author="Medi W. Assumani",
    author_email="mediassumani49@gmail.com",
    description="A lightweight web scrapping package tool built in Python.",
    url="https://github.com/MediBoss/Escrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
