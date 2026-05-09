const input = document.getElementById("messageInput");
const charCount = document.getElementById("charCount");
const analyzeBtn = document.getElementById("analyzeBtn");
const clearBtn = document.getElementById("clearBtn");
const historyTable = document.getElementById("historyTable");

let history = [];

input.addEventListener("input", () => {
  charCount.textContent = input.value.length;
});

clearBtn.addEventListener("click", () => {
  input.value = "";
  charCount.textContent = 0;
});

analyzeBtn.addEventListener("click", () => {
  const text = input.value.trim();
  if (!text) return;

  const isSpam = text.toLowerCase().includes("free") || text.toLowerCase().includes("win");

  const result = {
    id: history.length + 1,
    text,
    label: isSpam ? "SPAM" : "NOT SPAM",
    score: (Math.random() * 0.1 + 0.9).toFixed(4),
    date: new Date().toLocaleString()
  };

  updateResult(result);
  history.unshift(result);
  renderHistory();
});

function updateResult(result) {
  document.getElementById("resultLabel").textContent = result.label;
  document.getElementById("resultDesc").textContent =
    result.label === "SPAM"
      ? "Сообщение является спамом"
      : "Сообщение не является спамом";

  document.getElementById("scorePercent").textContent =
    Math.round(result.score * 100) + "%";

  document.getElementById("labelValue").textContent = result.label;
  document.getElementById("scoreValue").textContent = result.score;
  document.getElementById("dateValue").textContent = result.date;
}

function renderHistory() {
  historyTable.innerHTML = "";

  history.slice(0, 5).forEach((item) => {
    const row = `
      <tr>
        <td>${item.id}</td>
        <td>${item.text}</td>
        <td>${item.label}</td>
        <td>${item.score}</td>
        <td>${item.date}</td>
      </tr>
    `;
    historyTable.innerHTML += row;
  });
}