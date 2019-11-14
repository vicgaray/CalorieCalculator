import tkinter as tk


class CalorieWindow:

    def __init__(self, window):

        # Important variables
        self.active_level = None
        self.diet_cal = None

        # Initializes Window
        self.window = window

        # Initializes all Labels
        self.warning_label = tk.Label(
            self.window, text="* Measurements are based on the english system", fg="red")

        self.age_label = tk.Label(self.window, text="AGE:")
        self.weight_label = tk.Label(self.window, text="WEIGHT(lbs):")
        self.height_label = tk.Label(self.window, text="HEIGHT(in):")

        self.maintain_label = tk.Label(
            self.window, text="* Default is maintaining. Don't choose anything if maintaing.", fg="red")

        self.calorie_label = tk.Label(self.window, text="")

        # Initializes all Entries
        self.age_entry = tk.Entry(self.window, bd=1)
        self.weight_entry = tk.Entry(self.window, bd=1)
        self.height_entry = tk.Entry(self.window, bd=1)

        # Initializes all Radiobuttons
        # Activity level Radiobuttons
        self.activity = tk.DoubleVar()
        self.sedentary = tk.Radiobutton(self.window, text="sedentray",
                                        variable=self.activity, value=1.2)
        self.light_active = tk.Radiobutton(self.window, text="light activity",
                                           variable=self.activity, value=1.375)
        self.moderately_active = tk.Radiobutton(self.window, text="moderately_active",
                                                variable=self.activity, value=1.55)
        self.very_active = tk.Radiobutton(self.window, text="very active",
                                          variable=self.activity, value=1.725)
        self.extra_active = tk.Radiobutton(self.window, text="extra active",
                                           variable=self.activity, value=1.9)
        # Diet amount Radiobuttons
        self.diet = tk.IntVar()
        self.aggressive_cut = tk.Radiobutton(self.window, text="aggressive cut",
                                             variable=self.diet, value=-300)
        self.light_cut = tk.Radiobutton(self.window, text="light cut",
                                        variable=self.diet, value=-100)
        self.light_bulk = tk.Radiobutton(self.window, text="light bulk",
                                         variable=self.diet, value=350)
        self.aggressive_bulk = tk.Radiobutton(self.window, text="aggressive bulk",
                                              variable=self.diet, value=500)

        # Initializes all Buttons
        self.submit_button = tk.Button(self.window, text="Submit")

    def create_frame(self):
        """Positions and sets up everything in the window."""

        # Positions labels
        self.warning_label.grid(column=0, row=0, columnspan=2)

        self.age_label.grid(row=1, sticky="W")
        self.weight_label.grid(row=2, sticky="W")
        self.height_label.grid(row=3, sticky="W")

        self.maintain_label.grid(column=0, row=7, columnspan=2)

        self.calorie_label.grid(column=1, row=11)

        # Positions Entries
        self.age_entry.grid(column=1, row=1)
        self.weight_entry.grid(column=1, row=2)
        self.height_entry.grid(column=1, row=3)

        # Positions Radiobuttons and sets the command for selecting them.
        # Activity level Radiobuttons
        self.sedentary.grid(row=4)
        self.sedentary['command'] = lambda lvl=self.activity: self.set_active_level(lvl)

        self.light_active.grid(row=5)
        self.light_active['command'] = lambda lvl=self.activity: self.set_active_level(lvl)

        self.moderately_active.grid(row=6)
        self.moderately_active['command'] = lambda lvl=self.activity: self.set_active_level(lvl)

        self.very_active.grid(column=1, row=4)
        self.very_active['command'] = lambda lvl=self.activity: self.set_active_level(lvl)

        self.extra_active.grid(column=1, row=5)
        self.extra_active['command'] = lambda lvl=self.activity: self.set_active_level(lvl)

        # Diet calorie amount Radiobuttons
        self.aggressive_cut.grid(row=8)
        self.aggressive_cut['command'] = lambda amount=self.diet: self.set_diet(amount)

        self.light_cut.grid(row=9)
        self.light_cut['command'] = lambda amount=self.diet: self.set_diet(amount)

        self.light_bulk.grid(column=1, row=8)
        self.light_bulk['command'] = lambda amount=self.diet: self.set_diet(amount)

        self.aggressive_bulk.grid(column=1, row=9)
        self.aggressive_bulk['command'] = lambda amount=self.diet: self.set_diet(amount)

        # Create an Button
        self.submit_button.grid(column=1, row=10)
        self.submit_button['command'] = self.result

    def set_diet(self, amount):
        """"Sets the diet_cal by getting the value of the diet Radiobuttons"""
        self.diet_cal = amount.get()

    def set_active_level(self, lvl):
        """Sets the active_level by getting the value of the activity level Radiobutton"""
        self.active_level = lvl.get()

    def result(self):
        """Gets the final calorie for the Person."""
        try:
            p = Person(int(self.age_entry.get()), int(self.height_entry.get()),
                       int(self.weight_entry.get()), self.active_level, self.diet_cal)
            output = p.calorie()
        except:
            output = "Propertly put all inputs needed."

        self.calorie_label.config(text=output)
        self.reset()

    def reset(self):
        """Reset everything in the window."""
        # Resests important variables
        self.active_level = None
        self.diet_cal = None

        # Resets entries
        self.age_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)

        # Deselect activity level Radiobuttons
        self.sedentary.deselect()
        self.light_active.deselect()
        self.moderately_active.deselect()
        self.very_active.deselect()
        self.extra_active.deselect()

        # Deselect diet amount Radiobuttons
        self.aggressive_cut.deselect()
        self.light_cut.deselect()
        self.light_bulk.deselect()
        self.aggressive_bulk.deselect()


class Person:
    def __init__(self, age, height, weight, active_level, diet):
        self.age = age
        self.height = height
        self.weight = weight
        self.active_level = active_level
        self.diet = diet

    def calorie(self):
        """Calculates the persons base calories."""
        c = 66 + (6.3 * self.weight) + (12.9 * self.height) - (6.8 * self.age)

        # If they chose a diet amount, default is maintain
        if self.diet:
            return int((c * self.active_level) + self.diet)

        return int(c * self.active_level)


window = tk.Tk()

launch = CalorieWindow(window)
launch.create_frame()

window.mainloop()
