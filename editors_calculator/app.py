import tkinter as tk
from tkinter import ttk, messagebox

from editors_calculator.constants import (NUMBER_OF_SYMBOLS_LABEL, RATE_PER_PAGE_LABEL,
                                          CALCULATE_BUTTON_TEXT, FEE_INDICATOR_LABEL,
                                          INVALID_INPUT_MESSAGE, SYMBOLS_PER_PAGE,
                                          FEE_VALUE, INVALID_INPUT_MESSAGE_TITLE, DEDUCTION_LABEL)


class Calculator(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fee_value = tk.StringVar()
        self.deduction_value = tk.StringVar(value="6")

        self.style = ttk.Style()
        self.style.configure("TButton", font=("TkDefaultFont", 14))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        symbols_entry_label = ttk.Label(self, text=NUMBER_OF_SYMBOLS_LABEL, font=("TkDefaultFont", 10))
        symbols_entry_label.place(relx=0.4, rely=0.15, anchor="center")

        self.symbols_input_field = ttk.Entry(self, width=10)
        self.symbols_input_field.place(relx=0.6, rely=0.15, anchor="center")

        rate_per_page_label = ttk.Label(self, text=RATE_PER_PAGE_LABEL, font=("TkDefaultFont", 10))
        rate_per_page_label.place(relx=0.4, rely=0.3, anchor="center")

        self.rate_per_page_input_field = ttk.Entry(self, width=10)
        self.rate_per_page_input_field.place(relx=0.6, rely=0.3, anchor="center")

        deduction_label = ttk.Label(self, text=DEDUCTION_LABEL, font=("TkDefaultFont", 10))
        deduction_label.place(relx=0.4, rely=0.45, anchor="center")

        self.deduction_input_field = ttk.Entry(self, width=10, textvariable=self.deduction_value)
        self.deduction_input_field.place(relx=0.6, rely=0.45, anchor="center")

        self.calculate_button = ttk.Button(self, text=CALCULATE_BUTTON_TEXT, command=self.calculate_fee,
                                           cursor="hand2", style="TButton")
        self.calculate_button.place(relx=0.5, rely=0.65, anchor="center")

        fee_indicator_label = ttk.Label(self, text=FEE_INDICATOR_LABEL, font=("TkDefaultFont", 12))
        fee_indicator_label.place(relx=0.4, rely=0.84, anchor="center")

        self.fee_value_label = ttk.Label(self, textvariable=self.fee_value, font=("TkDefaultFont", 12, "bold"))
        self.fee_value_label.place(relx=0.6, rely=0.84, anchor="center")

    def calculate_fee(self):
        symbols_value = self.symbols_input_field.get()
        symbols_value = symbols_value.replace(" ", "")
        try:
            rate_per_page_value = float(self.rate_per_page_input_field.get())
            deduction_rate = float(self.deduction_value.get())
            if not symbols_value.isnumeric():
                self.show_popup()
                return
            fee_value = float(symbols_value) / SYMBOLS_PER_PAGE * float(rate_per_page_value)
            deduction = fee_value * deduction_rate / 100
            fee_value -= deduction
            fee = f"{fee_value:.02f}"
            self.fee_value.set(FEE_VALUE.format(value=fee))
            print(self.deduction_value.get())
        except ValueError:
            self.show_popup()

    def show_popup(self):
        message = messagebox.Message(parent=self, title=INVALID_INPUT_MESSAGE_TITLE, message=INVALID_INPUT_MESSAGE)
        message.show()
