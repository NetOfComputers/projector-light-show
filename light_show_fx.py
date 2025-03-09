import json
class LSFX:
    def __init__(self):
        # load effects from json file
        with open('fx.json') as f:
            self.fx = json.load(f)

    