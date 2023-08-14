from kivy.app import App
from grille_couleur import GrilleCouleurs


class GrilleApp(App):
    def build(self):
        return GrilleCouleurs()


if __name__ == "__main__":
    GrilleApp().run()
