from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.core.window import Window
w=Window.size = 400,600
KV = '''
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer

BoxLayout:

    # CodeInput:
    #     lexer: KivyLexer()
    #     style_name: "native"
    #     on_text: app.update_kv_file(self.text)
    #     size_hint_x: .6

    HotReloadViewer:
      
        size_hint_x: .3
        path: app.path_to_kv_file
        errors: True
        errors_text_color: 1, 0, 0, 1
        errors_background_color: app.theme_cls.bg_light
      
        
'''


class Example(MDApp):
    path_to_kv_file = "kv_file_s.kv"

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepOrange"
        self.custom_name = 'asdfsd'
        return Builder.load_string(KV)
    
    

    def update_kv_file(self, text):
        with open(self.path_to_kv_file, "w") as kv_file:
            kv_file.write(text)

    
Example().run()