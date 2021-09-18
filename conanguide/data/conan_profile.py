import collections


class ConanProfile:
    def __init__(self):
        self.settings = collections.OrderedDict()
        self.options = collections.OrderedDict()
        self.build_requires = collections.OrderedDict()
        self.environments = collections.OrderedDict()

    def get_text(self) -> str:

        profile_text: list = list()  # List of strings

        # --- Settings
        profile_text.append("[settings]")
        for key, value in self.settings.items():
            profile_text.append(key + "=" + value)

        # --- Options
        profile_text.append("[options]")
        for key, value in self.options.items():
            profile_text.append(key + "=" + value)

        # --- Build Requires
        profile_text.append("[build_requires]")
        for key, value in self.build_requires.items():
            profile_text.append(key)

        # --- Environments
        profile_text.append("[env]")
        for key, value in self.environments.items():
            profile_text.append(key + "=" + value)

        return "\n".join(profile_text)
