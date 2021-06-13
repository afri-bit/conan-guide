import os

from conans.client.conan_api import Conan
from conanguide.data.conan_recipe import *


class ConanApi(Conan):
    """
    Extension of the conan client Python API
    """
    def __init__(self):
        super().__init__()

    def get_all_recipes(self) -> list:
        """
        Get the all the recipes from the conan local cache
        :return list<RecipeInfo>: List of recipe info object, contains name, version, user and channel information
        """
        recipes = list()

        # Search all the recipes by using 'None' as input parameter
        conan_recipes = self.search_recipes(None)

        # Check if the return value contains error
        # The return values are packed in a dictionary. One of the key gives the error status
        if conan_recipes["error"] is False and len(conan_recipes["results"]) > 0:
            recipe_items = conan_recipes["results"][0]["items"]

            # Iterate through all recipes and convert it to RecipeInfo object
            for r in recipe_items:
                recipe_id = r["recipe"]["id"]
                recipes.append(RecipeInfo.create_recipe_obj(recipe_id))

        return recipes

    def get_cache_folder(self) -> str:
        """
        Simplified function to return the local cache path
        :return cache_folder: Absolute path to the local cache directory
        """
        return self.factory()[0].cache_folder

    def get_package_list(self, recipe_id: str) -> list:
        """
        Simplified function to return packages that belongs to a recipe
        :param recipe_id: ID of the recipe to search for packages 'name/version@user/channel'
        :return list<dict>: list of dictionaries that contains all the information about the package
        """
        return self.search_packages(recipe_id)["results"][0]["items"][0]["packages"]

    def get_package_cache_path(self, recipe_id: str, package_hash: str) -> [str, str]:
        """
        Function to return the package path and package real path based on the recipe ID and its hash.
        On Windows there is an issue regarding the length of the path, so user has to change the conan settings in order
        to come around this issue, which splits the package content and the real path of the package itself using a
        reference link.
        This can return exact same values, depends on the configuration
        :param recipe_id: ID of the recipe to search for packages 'name/version@user/channel'
        :param package_hash: Package hash id to be searched
        :return real_path - str: The real path of the conan local cache
                package_path - str: Path to the content of the package
        """
        real_path = ""
        package_path = ""

        # Build an object out of the recipe id, so we don't have work with string
        recipe_obj = RecipeInfo.create_recipe_obj(recipe_id)

        # Get the data path, normally its located under 'cache_folder/data'
        data_path = os.path.join(os.path.abspath(self.get_cache_folder()), "data")

        # Build the path based on recipe info
        recipe_path = os.path.normpath(recipe_obj.name + "/" + recipe_obj.version)

        # Check if the recipe contains user and channel information
        if recipe_obj.attribute is None:  # No user and channel information
            recipe_path = os.path.join(recipe_path, os.path.normpath("_/_"))
        else:  # Recipe has user and channel information
            recipe_path = os.path.join(recipe_path, os.path.normpath(recipe_obj.attribute.get_info()))

        recipe_path = os.path.join(data_path, recipe_path)

        real_path = os.path.join(recipe_path, os.path.normpath("package/" + package_hash))

        # Check if the package real path contains '.conan_link' file, where the reference link is stored
        if os.path.isfile(os.path.join(real_path, ".conan_link")):
            conan_link = os.path.join(real_path, ".conan_link")

            with open(conan_link) as f:
                # Package path will be filled with the information from the file
                package_path = f.readline()
        else:  # No reference link, the content of the package is located directly under the real path
            package_path = real_path

        return real_path, package_path
