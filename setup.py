import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="date_tools",
    version="0.0.2",
    author="Henin Roland Karkada",
    author_email="henin.roland@gmail.com",
    description="Date utilities to guess the date format given any date string or list of date strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/henin/date_tools",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
