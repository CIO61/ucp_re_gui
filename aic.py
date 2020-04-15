import param_types


class aic:
    def __init__(self):
        self.Name = None
        self.Description = None
        self.CustomName = None
        self.Personality = {
            paramname: None for paramname in param_types.param_names
        }
