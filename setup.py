import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="damm32",
    version="0.0.1",
    author="Dan Trickey",
    author_email="contact@trickey.io",
    description="A pure-python implementation of the Damm Algorithm, base 32",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trickeydan/damm32",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
