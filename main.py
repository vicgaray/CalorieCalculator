import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup

class Person:
    def __init__(self, age, height, weight, active_level, diet):
        self.age = age
        self.height = height
        self.weight = weight
        self.active_level = active_level
        self.diet = diet

    def calorie(self):
        """Calculates the persons calories."""
        print(self.age, self.height, self.weight, self.active_level, self.diet)
        c = 66 + (6.3 * self.weight) + (12.9 * self.height) - (6.8 * self.age)

        # If they chose a diet amount, default is maintain
        return int((c * self.active_level) + self.diet)

class ErrorPop(Popup):
    pass

class MyGrid(Widget):
    age = ObjectProperty(None)
    weight = ObjectProperty(None)
    h = ObjectProperty(None)
    act_lvl = NumericProperty(0)
    diet = NumericProperty(0)
    cal = StringProperty("")

    def set_diet_cal(self, value):
        """Gives the diet a value as it's selected"""
        self.diet = value

    def set_active_level(self, value):
        """Gives a active level as it's selected."""
        self.act_lvl = value

    def clear_act_lvl(self):
        """Clears active level if button gets deselected."""
        self.act_lvl = 0

    def result(self):
        """Prepares the result to be shown or warns of invalid inputs."""
        try:
            if self.act_lvl:
                p = Person(int(self.age.text), int(self.h.text),
                       int(self.weight.text), self.act_lvl, self.diet)
                output = str(p.calorie())
                self.cal = output
            else:
                pops = ErrorPop()
                pops.open()

                self.cal = ""
        except:
            pops = ErrorPop()
            pops.open()

            self.cal = ""

        self.clear()

    def clear(self):
        """Resests the TextInputs."""
        self.age.text = ""
        self.h.text = ""
        self.weight.text = ""

class MyApp(App):

     def build(self):
         return MyGrid()

if __name__ == "__main__":
    MyApp().run()
