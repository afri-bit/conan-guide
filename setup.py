from setuptools import setup, find_packages


def get_requirements(filename):
    requirements = []
    with open(filename, "rt") as req_file:
        for line in req_file.read().splitlines():
            if not line.strip().startswith("#"):
                requirements.append(line)
    return requirements


project_requirements = get_requirements("requirements.txt")

setup(
    name="conan-blade",
    version="1.0.0",
    url="https://github.com/afri-bit/conan-blade",
    license="MIT",
    author="Afrizal Herlambnag",
    author_email="afri.bit@outlook.com",
    description="Qt based Graphical User Interface (GUI) to interact with conan package manager",

    packages=find_packages(),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For the detail information please refer to
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=project_requirements,

    # Project relation
    keywords=["conan", "conan.io", "GUI", "Conan GUI", "PyQt5"],

    entry_points={
        "console_scripts": [
            "conan-blade=conanblade.app:main"
        ]
    }
)
