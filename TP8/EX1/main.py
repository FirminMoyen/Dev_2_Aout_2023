from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class Calculator(BoxLayout):
    first_number = ObjectProperty(None)
    second_number = ObjectProperty(None)
    result = StringProperty('')
    operation = StringProperty('add')

    def calculate(self):
        # Vérification des entrées
        try:
            num1 = float(self.first_number.text)
            num2 = float(self.second_number.text)
        except ValueError:
            self.show_error('Veuillez entrer des nombres valides.')
            return

        if self.operation == 'add':
            self.result = str(num1 + num2)
        elif self.operation == 'subtract':
            self.result = str(num1 - num2)
        elif self.operation == 'multiply':
            self.result = str(num1 * num2)
        elif self.operation == 'divide':
            if num2 == 0:
                self.show_error("La division par zéro n'est pas autorisée.")
                return
            self.result = str(num1 / num2)

    def show_error(self, message):
        popup = Popup(title='Erreur',
                      content=Label(text=message),
                      size_hint=(0.5, 0.5))
        popup.open()


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == '__main__':
    CalculatorApp().run()
