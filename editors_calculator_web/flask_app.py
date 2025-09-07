from flask import Flask, render_template, request
from editors_calculator_web import constants
from editors_calculator_web.calculator_logic import  calculate_fee

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            symbols_value = request.form.get("symbols")
            rate_per_page_value = float(request.form.get("rate"))
            deduction_rate = float(request.form.get("deduction"))
            mode = request.form.get("mode")

            result = calculate_fee(symbols_value, rate_per_page_value, deduction_rate, mode)
        except Exception:
            error = constants.INVALID_INPUT_MESSAGE

    return render_template(
        "index.html",
        constants=constants,
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
