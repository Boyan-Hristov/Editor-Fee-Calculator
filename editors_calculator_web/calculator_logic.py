from editors_calculator_web import constants

def calculate_fee(symbols_value: str, rate_per_page_value: float, deduction_rate: float, mode: str):
    symbols_value = symbols_value.replace(" ", "")
    if not symbols_value.isnumeric():
        raise ValueError("Invalid input: symbols must be numeric")
    divisor = constants.SYMBOLS_PER_PAGE if mode == constants.NUMBER_OF_SYMBOLS else 1
    fee_value = float(symbols_value) / divisor * float(rate_per_page_value)
    deduction = fee_value * deduction_rate / 100
    fee_value -= deduction
    fee = f"{fee_value:.02f}"
    euro_value = f"{float(fee) * constants.EUR_TO_BGN:.02f}"
    return constants.FEE_VALUE.format(lev_value=fee, euro_value=euro_value)

