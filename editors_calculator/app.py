import tkinter as tk
from tkinter import ttk, messagebox

from editors_calculator import constants


class Calculator(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fee_value = tk.StringVar()
        self.deduction_value = tk.StringVar(value=constants.DEFAULT_DEDUCTION_RATE)

        self.style = ttk.Style()
        self.style.configure("TButton", font=("TkDefaultFont", 14))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.symbols_or_pages_dropdown = ttk.Combobox(self, values=constants.DROPDOWN_OPTIONS, width=14)
        self.symbols_or_pages_dropdown.set(constants.NUMBER_OF_SYMBOLS)
        self.symbols_or_pages_dropdown.place(relx=0.37, rely=0.15, anchor="center")

        self.symbols_input_field = ttk.Entry(self, width=10)
        self.symbols_input_field.place(relx=0.6, rely=0.15, anchor="center")

        rate_per_page_label = ttk.Label(self, text=constants.RATE_PER_PAGE_LABEL, font=("TkDefaultFont", 10))
        rate_per_page_label.place(relx=0.34, rely=0.3, anchor="center")

        self.rate_per_page_input_field = ttk.Entry(self, width=10)
        self.rate_per_page_input_field.place(relx=0.6, rely=0.3, anchor="center")

        deduction_label = ttk.Label(self, text=constants.DEDUCTION_LABEL, font=("TkDefaultFont", 10))
        deduction_label.place(relx=0.4, rely=0.45, anchor="center")

        self.deduction_input_field = ttk.Entry(self, width=10, textvariable=self.deduction_value)
        self.deduction_input_field.place(relx=0.6, rely=0.45, anchor="center")

        self.calculate_button = ttk.Button(self, text=constants.CALCULATE_BUTTON_TEXT, command=self.calculate_fee,
                                           cursor="hand2", style="TButton")
        self.calculate_button.place(relx=0.5, rely=0.65, anchor="center")

        fee_frame = ttk.Frame(self)
        fee_frame.place(relx=0.5, rely=0.84, anchor="center")
        fee_frame.columnconfigure(0, weight=1)
        fee_frame.columnconfigure(1, weight=1)

        fee_indicator_label = ttk.Label(fee_frame, text=constants.FEE_INDICATOR_LABEL, font=("TkDefaultFont", 12))
        fee_indicator_label.grid(row=0, column=0, sticky="e", padx=5)

        self.fee_value_label = ttk.Label(fee_frame, textvariable=self.fee_value, font=("TkDefaultFont", 12, "bold"))
        self.fee_value_label.grid(row=0, column=1, sticky="w", padx=5)

    def calculate_fee(self):
        symbols_value = self.symbols_input_field.get()
        symbols_value = symbols_value.replace(" ", "")
        try:
            rate_per_page_value = float(self.rate_per_page_input_field.get())
            deduction_rate = float(self.deduction_value.get())
            if not symbols_value.isnumeric():
                self.show_popup()
                return
            divisor = (
                constants.SYMBOLS_PER_PAGE if self.symbols_or_pages_dropdown.get() == constants.NUMBER_OF_SYMBOLS
                else 1
            )
            fee_value = float(symbols_value) / divisor * float(rate_per_page_value)
            deduction = fee_value * deduction_rate / 100
            fee_value -= deduction
            fee = f"{fee_value:.02f}"
            euro_value = f"{float(fee) * constants.EUR_TO_BGN:.02f}"
            self.fee_value.set(constants.FEE_VALUE.format(lev_value=fee, euro_value=euro_value))
        except ValueError:
            self.show_popup()

    def show_popup(self):
        message = messagebox.Message(
            parent=self, title=constants.INVALID_INPUT_MESSAGE_TITLE, message=constants.INVALID_INPUT_MESSAGE
        )
        message.show()
