from setuptools import setup, find_packages


def get_requires(filename):
    requirements = []
    with open(filename, "rt") as req_file:
        for line in req_file.read().splitlines():
            if not line.strip().startswith("#"):
                requirements.append(line)
    return requirements


project_requirements = get_requires("requirements.txt")

setup(
    name="conan-blade",
    version="0.0.1",
    url="https://github.com/afri-bit/conan-blade",
    license="MIT",
    author="Afrizal Herlambnag",
    author_email="Afrizal.Herlambang@gmail.com",
    description="GUI application",

    packages=find_packages(),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip"s
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=project_requirements,

    # What does your project relate to?
    keywords=["conan", "conan.io", "GUI", "PyQt"],

    entry_points={
        "console_scripts": [
            "conan-blade=conanblade.app:main"
        ]
    }
)
