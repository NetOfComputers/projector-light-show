import json
import webview
class LSFX:
    def __init__(self, tkinter_app):
        # load effects from json file
        self.current_fx_index = 0
        with open('settings.json') as f:
            self.fx = json.load(f)

    def next_fx(self):
        # get the next effect
        self.current_fx_index = (self.current_fx_index + 1) % len(self.fx)
        return self.fx[self.current_fx_index]
    
    def get_current_fx(self):
        return self.fx[self.current_fx_index]
    
    def get_fx(self, index):
        return self.fx[index]

    def apply_current(self):
        webview.create_window("HTML Viewer", 'fx/web/party.html')
        webview.start()

    def apply_next(self):
        self.next_fx()

    
    # def get_fx_count(self):
    #     return len(self.fx)
    
    # def get_fx_names(self):
    #     return [fx['name'] for fx in self.fx]

    # def get_fx_by_name(self, name):
    #     for fx in self.fx:
    #         if fx['name'] == name:
    #             return fx
    #     return None
    # def get_fx_index_by_name(self, name):
    #     for i, fx in enumerate(self.fx):
    #         if fx['name'] == name:
    #             return i
    #     return None
