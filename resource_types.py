import param_types


class aic:
    def __init__(self):
        self.Name = None
        self.Description = None
        self.CustomName = None
        self.Personality = {
            paramname: None for paramname in param_types.param_names
        }


class TroopConfig:
    def __init__(self):
        self.Name = None
        self.Lord = {
            "StrengthMultiplier": None,
            "DotColour": None,
            "DotCount": None,
            "Type": None
        }
        self.normal = {
            "Units": [],
            "Counts:": []
        }
        self.crusader = {
            "Units": [],
            "Counts:": []
        }
        self.deathmatch = {
            "Units": [],
            "Counts:": []
        }