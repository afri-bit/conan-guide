"""
Script to generate python files from Qt .ui and .qrc files.
"""
import os

# Get the current script path with absolute path
script_path = os.path.abspath(os.path.dirname(__file__))

# List of ui files to be generated, the path must be relative to this path or absolute path
ui_files = [
    {"from": "../resources/ui/main_window.ui",
     "to": "../conanguide/ui/main/main_window_ui.py"},
    {"from": "../resources/ui/profile_attribute.ui",
     "to": "../conanguide/ui/widget/profile/profile_attribute_ui.py"},
    {"from": "../resources/ui/widget/tab/profile/tab_profile.ui",
     "to": "../conanguide/ui/widget/tab/profile/tab_profile_ui.py"},
    {"from": "../resources/ui/widget/tab/cache/tab_cache.ui",
     "to": "../conanguide/ui/widget/tab/cache/tab_cache_ui.py"},
    {"from": "../resources/ui/widget/tab/remote/tab_remote.ui",
     "to": "../conanguide/ui/widget/tab/remote/tab_remote_ui.py"},
    {"from": "../resources/ui/widget/tab/workspace/tab_workspace.ui",
     "to": "../conanguide/ui/widget/tab/workspace/tab_workspace_ui.py"},
    {"from": "../resources/ui/dialog/edit_name.ui",
     "to": "../conanguide/ui/dialog/edit/name/edit_name_ui.py"},
    {"from": "../resources/ui/dialog/edit_remote.ui",
     "to": "../conanguide/ui/dialog/edit/remote/edit_remote_ui.py"}
]

# List of resource files to be generated, the path must be relative to this path or absolute path
rc_files = [
    {"from": "../resources/resources.qrc", "to": "../conanguide/ui/res/resources_rc.py"}
]


def refactor_resource_import(file: str, replace_from: str, replace_with: str):
    with open(file, "r+") as f:
        code = f.read()
        code = code.replace(replace_from, replace_with)

        f.write(code)

        with open(file, "w") as g:
            g.write(code)


# Generate UI files
for ui in ui_files:
    cmd = ["pyside2-uic", "--from-imports"]

    if not os.path.isabs(ui["from"]):
        ui["from"] = os.path.abspath(os.path.join(script_path, ui["from"]))

    if not os.path.isabs(ui["to"]):
        ui["to"] = os.path.abspath(os.path.join(script_path, ui["to"]))

    cmd.append(ui["from"])
    cmd.append("-o")
    cmd.append(ui["to"])

    os.system(" ".join(cmd))

# Generate resources files
for rc in rc_files:
    cmd = ["pyside2-rcc"]

    if not os.path.isabs(rc["from"]):
        rc["from"] = os.path.abspath(os.path.join(script_path, rc["from"]))

    if not os.path.isabs(rc["to"]):
        rc["to"] = os.path.abspath(os.path.join(script_path, rc["to"]))

    cmd.append(rc["from"])
    cmd.append("-o")
    cmd.append(rc["to"])

    os.system(" ".join(cmd))

# Special treatment for the import of the UI files
refactor_resource_import(ui_files[0]["to"], "from  . import resources_rc", "from conanguide.ui.res import resources_rc")
refactor_resource_import(ui_files[1]["to"], "from  . import resources_rc", "from conanguide.ui.res import resources_rc")
refactor_resource_import(ui_files[2]["to"], "from  . import resources_rc", "from conanguide.ui.res import resources_rc")
refactor_resource_import(ui_files[3]["to"], "from  . import resources_rc", "from conanguide.ui.res import resources_rc")
refactor_resource_import(ui_files[4]["to"], "from  . import resources_rc", "from conanguide.ui.res import resources_rc")
refactor_resource_import(ui_files[5]["to"], "from  . import resources_rc", "from conanguide.ui.res import resources_rc")
refactor_resource_import(ui_files[6]["to"], "from  . import resources_rc", "from conanguide.ui.res import resources_rc")
refactor_resource_import(ui_files[7]["to"], "from  . import resources_rc", "from conanguide.ui.res import resources_rc")
