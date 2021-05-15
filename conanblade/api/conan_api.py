import os

from conans.client.conan_api import Conan
from conanblade.data.conan_recipe import *


class ConanApi(Conan):
    def __init__(self):
        super().__init__()

    def get_all_recipes(self) -> list:
        recipes = list()

        conan_recipes = self.search_recipes(None)

        if conan_recipes["error"] is False:
            recipe_items = conan_recipes["results"][0]["items"]

            for r in recipe_items:
                id = r["recipe"]["id"]
                recipes.append(self.build_recipe_obj(id))

        return recipes

    def get_cache_folder(self) -> str:
        return self.factory()[0].cache_folder

    def build_recipe_obj(self, recipe_id: str) -> RecipeInfo:

        recipe_info = recipe_id.split("@")

        recipe_attr = None

        if len(recipe_info) > 1:
            recipe_attr = recipe_info[1].split("/")
            recipe_attr = RecipeAttribute(recipe_attr[0], recipe_attr[1])

        recipe_info = recipe_info[0].split("/")

        return RecipeInfo(recipe_info[0], recipe_info[1], recipe_attr)

    def get_package_list(self, recipe_id: str) -> list:
        return self.search_packages(recipe_id)["results"][0]["items"][0]["packages"]

    def get_package_cache_path(self, recipe_id: str, package_hash: str) -> [str, str]:
        real_path = ""
        package_path = ""

        recipe_obj = self.build_recipe_obj(recipe_id)

        data_path = os.path.join(os.path.abspath(self.get_cache_folder()), "data")

        # Build the path based on recipe info
        recipe_path = os.path.normpath(recipe_obj.name + "/" + recipe_obj.version)
        if recipe_obj.attribute is None:
            recipe_path = os.path.join(recipe_path, os.path.normpath("_/_"))
        else:
            recipe_path = os.path.join(recipe_path, os.path.normpath(recipe_obj.attribute.get_info()))

        recipe_path = os.path.join(data_path, recipe_path)

        real_path = os.path.join(recipe_path, os.path.normpath("package/" + package_hash))

        if os.path.isfile(os.path.join(real_path, ".conan_link")):
            conan_link = os.path.join(real_path, ".conan_link")

            with open(conan_link) as f:
                package_path = f.readline()
        else:
            package_path = real_path

        return real_path, package_path

    @staticmethod
    def build_command_install(install_folder: str,
                              user: str,
                              channel: str,
                              profile: str,
                              params: str,
                              path_recipe: str) -> list:
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
    def build_command_build(build_folder: str,
                            install_folder: str,
                            package_folder: str,
                            source_folder: str,
                            params: str,
                            path_recipe: str) -> list:

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
    def build_command_source(source_folder: str, install_folder: str, path_recipe: str) -> list:
        cmd = ["conan", "source", os.path.abspath(path_recipe)]
        if source_folder != "":
            cmd.extend(["-sf", os.path.abspath(source_folder)])
        if install_folder != "":
            cmd.extend(["-if", os.path.abspath(install_folder)])

        return cmd

    @staticmethod
    def build_command_package(build_folder: str, install_folder: str, package_folder: str, source_folder: str,
                              path_recipe: str) -> list:
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
    def build_command_export(params: str, path_recipe: str) -> list:
        cmd = ["conan", "export", os.path.abspath(path_recipe)]
        if params != "":
            cmd.extend(params.split(" "))
        return cmd

    @staticmethod
    def build_command_export_package(build_folder: str, install_folder: str, package_folder: str,
                                     source_folder: str, params: str, path_recipe: str):
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
