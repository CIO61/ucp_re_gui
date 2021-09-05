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


class StartGoods:
    def __init__(self):
        self.description = {}
        self.normal = {
            "wood": 0,
            "stone": 0,
            "iron": 0,
            "pitch": 0,
            "wheat": 0,
            "hop": 0,
            "flour": 0,
            "beer": 0,
            "meat": 0,
            "fruit": 0,
            "cheese": 0,
            "bread": 0,
            "bows": 0,
            "crossbows": 0,
            "spears": 0,
            "pikes": 0,
            "maces": 0,
            "swords": 0,
            "leatherarmor": 0,
            "metalarmor": 0,
            "gold": {
                "human": [0, 0, 0, 0, 0],
                "ai": [0, 0, 0, 0, 0]
            }
        }
        self.crusader = {
            "wood": 0,
            "stone": 0,
            "iron": 0,
            "pitch": 0,
            "wheat": 0,
            "hop": 0,
            "flour": 0,
            "beer": 0,
            "meat": 0,
            "fruit": 0,
            "cheese": 0,
            "bread": 0,
            "bows": 0,
            "crossbows": 0,
            "spears": 0,
            "pikes": 0,
            "maces": 0,
            "swords": 0,
            "leatherarmor": 0,
            "metalarmor": 0,
            "gold": {
                "human": [0, 0, 0, 0, 0],
                "ai": [0, 0, 0, 0, 0]
            }
        }
        self.deathmatch = {
            "wood": 0,
            "stone": 0,
            "iron": 0,
            "pitch": 0,
            "wheat": 0,
            "hop": 0,
            "flour": 0,
            "beer": 0,
            "meat": 0,
            "fruit": 0,
            "cheese": 0,
            "bread": 0,
            "bows": 0,
            "crossbows": 0,
            "spears": 0,
            "pikes": 0,
            "maces": 0,
            "swords": 0,
            "leatherarmor": 0,
            "metalarmor": 0,
            "gold": {
                "human": [0, 0, 0, 0, 0],
                "ai": [0, 0, 0, 0, 0]
            }
        }
