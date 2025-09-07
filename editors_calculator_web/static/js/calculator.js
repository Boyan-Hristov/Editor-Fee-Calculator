const SYMBOLS_PER_PAGE = 1800;
const EUR_TO_BGN = 0.511292;

function calculateFee() {
  const mode = document.getElementById("mode").value;
  const symbolsValue = document.getElementById("symbols").value.replace(/\s/g, "");
  const rateValue = parseFloat(document.getElementById("rate").value);
  const deductionRate = parseFloat(document.getElementById("deduction").value);

  if (isNaN(rateValue) || isNaN(deductionRate) || isNaN(parseFloat(symbolsValue))) {
    alert("Моля, въведете числови стойности!");
    return;
  }

  const divisor = (mode === "symbols") ? SYMBOLS_PER_PAGE : 1;
  let feeValue = parseFloat(symbolsValue) / divisor * rateValue;
  let deduction = feeValue * deductionRate / 100;
  feeValue -= deduction;

  const lev = feeValue.toFixed(2);
  const euro = (feeValue * EUR_TO_BGN).toFixed(2);

  document.getElementById("result").innerText = `Хонорар: ${lev} лв. / € ${euro}`;
}
