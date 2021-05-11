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
