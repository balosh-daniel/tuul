#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = []

setup_requirements = []

test_requirements = []

setup(
    author="Daniel Balosh",
    author_email="no@gmail.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="python toolbox",
    entry_points={
        "console_scripts": [
            "tuul=tuul.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="tuul",
    name="tuul",
    packages=find_packages(include=["tuul", "tuul.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/daniel-balosh/tuul",
    # fmt: off
    version='0.14.1',
    # fmt: on
    zip_safe=False,
)
