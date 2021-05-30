import unittest
from conanguide.data.conan_recipe import *


class TestConanRecipeInfo(unittest.TestCase):
    def setUp(self):
        self.conan_package_attribute = RecipeAttribute("user", "testing")
        self.conan_package_info_attr = RecipeInfo("pack_foo", "1.0", self.conan_package_attribute)
        self.conan_package_info_noattr = RecipeInfo("pack_bar", "2.0")

    def test_recipe_info_with_attribute(self):
        self.assertEqual(self.conan_package_info_attr.get_info(), "pack_foo/1.0@user/testing")

    def test_recipe_attribute(self):
        self.assertEqual(self.conan_package_attribute.get_info(), "user/testing")

    def test_recipe_info_noattribute(self):
        self.assertEqual(self.conan_package_info_noattr.get_info(), "pack_bar/2.0")
