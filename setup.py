import pathlib

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


project_requirements = get_requirements("requirements.txt")

setup(
    name="conan-guide",
    version="1.1.2",
    description="Qt based Graphical User Interface (GUI) to interact with conan package manager",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/afri-bit/conan-guide",
    author="Afrizal Herlambang",
    author_email="afri.bit@outlook.com",
    license="MIT",
    packages=find_packages(),
    install_requires=project_requirements,

    # Project relation
    keywords=["conan", "conan.io", "GUI", "Conan GUI", "PySide2"],

    package_data={'': ['requirements.txt', 'resources/*']},

    entry_points={
        "console_scripts": [
            "conan-guide=conanguide.app:main"
        ]
    }
)
