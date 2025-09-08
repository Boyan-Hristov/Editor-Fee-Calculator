from editors_calculator.app import Calculator
from editors_calculator.constants import APP_TITLE


def main():
    app = Calculator()
    app.title(APP_TITLE)
    app.geometry("500x200")
    app.resizable(False, False)
    app.mainloop()
