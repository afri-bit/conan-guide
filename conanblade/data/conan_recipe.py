from abc import ABC, abstractmethod


class ConanRecipe(ABC):
    @abstractmethod
    def get_info(self):
        raise NotImplementedError


class RecipeAttribute(ConanRecipe):
    def __init__(self, user: str, channel: str):
        self.user = user
        self.channel = channel

    def get_info(self) -> str:
        return "{user}/{channel}".format(user=self.user, channel=self.channel)


class RecipeInfo(ConanRecipe):
    def __init__(self, name: str, version: str, attribute: RecipeAttribute = None):
        self.name = name
        self.version = version
        self.attribute = attribute

    def get_info(self) -> str:
        if self.attribute is None:
            return "{name}/{version}".format(name=self.name, version=self.version)

        return "{name}/{version}@{attribute}".format(name=self.name, version=self.version,
                                                     attribute=self.attribute.get_info())

    @classmethod
    def create_recipe_obj(cls, recipe_id: str):
        """
        Method to parse the string from the recipe ID and convert it to an object
        :param recipe_id: ID of a recipe to be converted to an object
        :return: RecipeInfo object
        """

        # Find out if the recipe ID has user and channel information (attribute)
        recipe_info = recipe_id.split("@")

        recipe_attr = None

        if len(recipe_info) > 1:  # Recipe id contains user and channel information
            recipe_attr = recipe_info[1].split("/")
            recipe_attr = RecipeAttribute(recipe_attr[0], recipe_attr[1])

        # Get name and version information
        recipe_info = recipe_info[0].split("/")

        return cls(recipe_info[0], recipe_info[1], recipe_attr)
