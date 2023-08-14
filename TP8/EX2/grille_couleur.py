from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class Cellule(Button):
    def __init__(self, **kwargs):
        super(Cellule, self).__init__(**kwargs)
        self.couleurs = [(1, 1, 1, 1), (1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1),
                         (0.5, 0.5, 0.5, 1)]  # blanc, rouge, vert, bleu, gris
        self.indice_couleur = 0
        self.background_color = self.couleurs[self.indice_couleur]
        self.bind(pos=self.update_couleur, size=self.update_couleur)

    def update_couleur(self, *args):
        self.background_color = self.couleurs[self.indice_couleur]

    def on_press(self):
        self.indice_couleur = (self.indice_couleur + 1) % len(self.couleurs)
        self.update_couleur()


class GrilleCouleurs(GridLayout):
    def __init__(self, **kwargs):
        super(GrilleCouleurs, self).__init__(**kwargs)
        self.cols = 5
        for i in range(25):
            cellule = Cellule()
            self.add_widget(cellule)
