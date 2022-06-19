from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.2'
DESCRIPTION = 'Multi-Criteria Decision Making'
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()


# Setting up
setup(
    name="Topsis-Pramit-101903198",
    version=VERSION,
    author="Pramit",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url = "https://github.com/Pramit29/Topsis-Pramit-101903198",
    license="MIT",
    packages=["Topsis_Pramit_101903198"],
    install_requires='pandas',
    include_package_data=True,
    keywords=['python', 'best model', 'Topsis', 'multi-criteria decision making', 'assignment'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "topsis=Topsis_Pramit_101903198.topsis_Pramit:main",
        ]
    },
)