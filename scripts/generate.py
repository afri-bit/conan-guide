"""
Script to generate python files from Qt .ui and .qrc files.
"""
import os

# Get the current script path with absolute path
script_path = os.path.abspath(os.path.dirname(__file__))

# List of ui files to be generated, the path must be relative to this path or absolute path
ui_files = [
    {"from": "../resources/ui/main_window.ui", "to": "../conanguide/ui/main/main_window_ui.py"},
    {"from": "../resources/ui/profile_attribute.ui", "to": "../conanguide/ui/widget/profile/profile_attribute_ui.py"}
]

# List of resource files to be generated, the path must be relative to this path or absolute path
rc_files = [
    {"from": "../resources/resources.qrc", "to": "../conanguide/ui/res/resources_rc.py"}
]

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
with open(ui_files[0]["to"], "r+") as f:
    code = f.read()
    code = code.replace("from  . import resources_rc", "from conanguide.ui.res import resources_rc")

    f.write(code)

    with open(ui_files[0]["to"], "w") as g:
        g.write(code)

with open(ui_files[1]["to"], "r+") as f:
    code = f.read()
    code = code.replace("from  . import resources_rc", "from conanguide.ui.res import resources_rc")

    f.write(code)

    with open(ui_files[1]["to"], "w") as g:
        g.write(code)
    pass