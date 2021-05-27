import os


class ConanCommandBuilder:
    """
    Class contains static methods to build conan command for CLI
    """

    @staticmethod
    def build_command_create(path_recipe: str,
                             user: str,
                             channel: str,
                             profile: str,
                             params: str) -> list:
        cmd = ["conan", "create", os.path.abspath(path_recipe)]

        if user != "" and channel != "":
            cmd.append(user + "/" + channel)
        if profile != "":
            cmd.extend(["-pr", profile])
        if params != "":
            cmd.extend(params.split(" "))

        return cmd

    @staticmethod
    def build_command_install(path_recipe: str,
                              install_folder: str,
                              user: str,
                              channel: str,
                              profile: str,
                              params: str) -> list:
        cmd = ["conan", "install", os.path.abspath(path_recipe)]
        if user != "" and channel != "":
            cmd.append(user + "/" + channel)
        if install_folder != "":
            cmd.extend(["-if", os.path.abspath(install_folder)])
        if profile != "":
            cmd.extend(["-pr", profile])
        if params != "":
            cmd.extend(params.split(" "))

        return cmd

    @staticmethod
    def build_command_build(path_recipe: str,
                            build_folder: str,
                            install_folder: str,
                            package_folder: str,
                            source_folder: str,
                            params: str) -> list:

        cmd = ["conan", "build", os.path.abspath(path_recipe)]
        if build_folder != "":
            cmd.extend(["-bf", os.path.abspath(build_folder)])
        if install_folder != "":
            cmd.extend(["-if", os.path.abspath(install_folder)])
        if package_folder != "":
            cmd.extend(["-pf", os.path.abspath(package_folder)])
        if source_folder != "":
            cmd.extend(["-sf", os.path.abspath(source_folder)])
        if params != "":
            cmd.extend(params.split(" "))
        return cmd

    @staticmethod
    def build_command_source(path_recipe: str, source_folder: str, install_folder: str, ) -> list:
        cmd = ["conan", "source", os.path.abspath(path_recipe)]
        if source_folder != "":
            cmd.extend(["-sf", os.path.abspath(source_folder)])
        if install_folder != "":
            cmd.extend(["-if", os.path.abspath(install_folder)])

        return cmd

    @staticmethod
    def build_command_package(path_recipe: str, build_folder: str,
                              install_folder: str, package_folder: str,
                              source_folder: str) -> list:
        cmd = ["conan", "package", os.path.abspath(path_recipe)]
        if build_folder != "":
            cmd.extend(["-bf", os.path.abspath(build_folder)])
        if install_folder != "":
            cmd.extend(["-if", os.path.abspath(install_folder)])
        if package_folder != "":
            cmd.extend(["-pf", os.path.abspath(package_folder)])
        if source_folder != "":
            cmd.extend(["-sf", os.path.abspath(source_folder)])
        return cmd

    @staticmethod
    def build_command_export(path_recipe: str, params: str) -> list:
        cmd = ["conan", "export", os.path.abspath(path_recipe)]
        if params != "":
            cmd.extend(params.split(" "))
        return cmd

    @staticmethod
    def build_command_export_package(path_recipe: str, build_folder: str, install_folder: str, package_folder: str,
                                     source_folder: str, params: str):
        cmd = ["conan", "export-pkg", os.path.abspath(path_recipe)]
        if build_folder != "":
            cmd.extend(["-bf", os.path.abspath(build_folder)])
        if install_folder != "":
            cmd.extend(["-if", os.path.abspath(install_folder)])
        if package_folder != "":
            cmd.extend(["-pf", os.path.abspath(package_folder)])
        if source_folder != "":
            cmd.extend(["-sf", os.path.abspath(source_folder)])
        if params != "":
            cmd.extend(params.split(" "))

        return cmd
