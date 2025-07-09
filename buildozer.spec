from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivy.lang import Builder

KV = '''
<FindixLayout>:
    orientation: 'vertical'
    padding: dp(20)
    spacing: dp(10)
    canvas.before:
        Color:
            rgba: (0.1, 0.1, 0.1, 1)
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: 'assets/logo.png'
        size_hint_y: None
        height: dp(150)

    Label:
        id: search_label
        text: 'Recherche de lieu'
        font_size: '20sp'
        color: (1, 0.8, 0, 1)

    TextInput:
        id: search_input
        hint_text: 'Tapez le mot-clé...'
        size_hint_y: None
        height: dp(40)

    Button:
        id: search_button
        text: 'Chercher'
        size_hint_y: None
        height: dp(40)
        background_color: (0.8, 0, 0, 1)

    Button:
        text: '🌐 FR / EN'
        size_hint_y: None
        height: dp(40)
        on_press: root.toggle_language()
'''

Builder.load_string(KV)

class FindixLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if platform in ("android", "ios"):
            from jnius import autoclass
            Locale = autoclass('java.util.Locale')
            lang = Locale.getDefault().getLanguage()
        else:
            import locale
            lang = locale.getdefaultlocale()[0][:2]
        if lang == 'fr':
            self.ids.search_label.text = "Recherche de lieu"
            self.ids.search_button.text = "Chercher"
        else:
            self.ids.search_label.text = "Place Search"
            self.ids.search_button.text = "Search"

    def toggle_language(self):
        if self.ids.search_label.text == "Recherche de lieu":
            self.ids.search_label.text = "Place Search"
            self.ids.search_button.text = "Search"
        else:
            self.ids.search_label.text = "Recherche de lieu"
            self.ids.search_button.text = "Chercher"

class FindixApp(App):
    def build(self):
        return FindixLayout()

if __name__ == '__main__':
    FindixApp().run()
