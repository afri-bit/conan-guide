import os
import pathlib
import re

from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


def get_requirements(filename):
    requirements = []
    with open(filename, "rt") as req_file:
        for line in req_file.read().splitlines():
            if not line.strip().startswith("#"):
                requirements.append(line)
    return requirements


def get_version():
    """ Get application version from the metadata file """
    filename = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                            "conanguide", "info.py"))
    with open(filename, "rt") as info_file:
        conanguide_info = info_file.read()
        version = re.search(r'__version__ = "([0-9a-z.-]+)"', conanguide_info).group(1)
        return version


project_requirements = get_requirements("requirements.txt")

setup(
    name="conan-guide",
    version=get_version(),
    description="Qt based Graphical User Interface (GUI) to interact with local cache of conan package manager",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/afri-bit/conan-guide",
    author="Afrizal Herlambang",
    author_email="afri.bit@outlook.com",
    license="MIT",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Environment :: X11 Applications :: Qt",
        "Environment :: Win32 (MS Windows)",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Linux"
    ],

    packages=find_packages(),
    install_requires=project_requirements,

    # Project relation
    keywords=["conan", "conan.io", "GUI", "Conan GUI", "PySide2"],

    package_data={"": ["requirements.txt", "resources/*"]},

    entry_points={
        "console_scripts": [
            "conan-guide=conanguide.app:main"
        ]
    }
)

