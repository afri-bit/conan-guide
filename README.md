# Conan GUIde

![](https://img.shields.io/pypi/v/conan-guide)
![](https://img.shields.io/pypi/pyversions/conan-guide)

**Conan GUIde** is Qt based Graphical User Interface (GUI) to interact with local cache of conan package manager. **Conan GUIde** provides user an easy overview of the information from the local cache without any further effort of typing in the terminal. User can find, copy and even open the path of the package with minimal effort and clicks.

With **Conan GUIde** user has also possibility to add, edit and remove local profiles and remotes of the conan package manager.

One of the core features from this application is the [workspace section](#tab-workspace), that allows user to execute the conan development flow from the existing conan recipe. User can also save the configuration into a file and load it back into workspace. See more in [Tab Workspace](#tab-workspace).

![](https://raw.githubusercontent.com/afri-bit/conan-guide/main/doc/img/tab_cache.png)

**!!! <u>WARNING</u> !!!**  
This application is mostly tested in Windows 10 environment. Linux Ubuntu users will have to expect deviated UI representation.  
Basic features and functionalitis work well in Linux Ubuntu 18.04 environment.

## Table of Content
- [Conan GUIde](#conan-guide)
  - [Table of Content](#table-of-content)
  - [Requirements](#requirements)
  - [Features](#features)
    - [Tab Cache](#tab-cache)
    - [Tab Workspace](#tab-workspace)
    - [Tab Profile](#tab-profile)
    - [Tab Remote](#tab-remote)
  - [Usage](#usage)
    - [Installation using Repository](#installation-using-repository)
    - [Installation using PyPI](#installation-using-pypi)
  - [Contribution](#contribution)
  - [License](#license)

## Requirements
* Python >= 3.5
* Conan >= 1.35 - `pip install conan`
* PySide2 - `pip install PySide2`
* Operating System with activated GUI

## Features
**Conan GUIde** consist multiple tabs, where each tab has a certain area of functionalities. 


### Tab Cache

![](https://raw.githubusercontent.com/afri-bit/conan-guide/main/doc/img/tab_cache.png)

**Tab Cache** provides list of recipes and packages, that are installed in the local cache. By selecting one of the recipes or packages, user can see more detailed information, such as description, compiler, architecture, version, `build_type` and further more.

Another important feature for Windows users is information about the data path and the actual package path. This feature saves time for Windows users due to the path separation between the data and the package itself. The package will be stored in the same path as the data path, it only save the reference link, that points to the other directory.

### Tab Workspace

![](https://raw.githubusercontent.com/afri-bit/conan-guide/main/doc/img/tab_workspace.png)

In this section user can configure their workspace and all the needed parameters to build their conan project. **Tab Workspace** also allows users to save their configuration and load it back to this section.

The console widget provides the information during the build process of the conan project.

### Tab Profile

![](https://raw.githubusercontent.com/afri-bit/conan-guide/main/doc/img/tab_profile.png)

The local profiles are listed in this section. User has the capability to add a new empty profile, rename and remove an existing profile. The content of the profile itself can also be edited using the application. 

### Tab Remote

![](https://raw.githubusercontent.com/afri-bit/conan-guide/main/doc/img/tab_remote.png)

## Usage
### Installation using Repository
```
git clone https://github.com/afri-bit/conan-guide.git
cd conan-guide
pip install .

# Start Conan GUIde
conan-guide
```

### Installation using [PyPI](https://pypi.org/)

```
pip install conan-guide
```

## Contribution
Please refer to [Contributing](https://github.com/afri-bit/conan-guide/blob/main/CONTRIBUTING.md).

## License
**Conan GUIde** is licensed under the [MIT](https://github.com/afri-bit/conan-guide/blob/main/LICENSE) license.  
Copyright © 2021, Afrizal Herlambang
