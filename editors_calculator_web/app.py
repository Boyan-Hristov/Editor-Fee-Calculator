from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

SYMBOLS_PER_PAGE = 1800
EUR_TO_BGN = 0.511292

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    try:
        symbols_or_pages = data.get("symbols_or_pages", "symbols")
        symbols_value = data.get("symbols", "").replace(" ", "")
        rate = float(data.get("rate", 0))
        deduction_rate = float(data.get("deduction", 6))

        divisor = SYMBOLS_PER_PAGE if symbols_or_pages == "symbols" else 1
        fee_value = float(symbols_value) / divisor * rate
        deduction = fee_value * deduction_rate / 100
        fee_value -= deduction
        fee = f"{fee_value:.02f}"
        euro_value = f"{float(fee) * EUR_TO_BGN:.02f}"
        result = f"{fee} лв. / € {euro_value}"
    except Exception:
        result = "Невалидни входни данни!"

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
