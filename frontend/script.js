const API_URL = "http://127.0.0.1:8000";

const input = document.getElementById("messageInput");
const charCount = document.getElementById("charCount");
const analyzeBtn = document.getElementById("analyzeBtn");
const clearBtn = document.getElementById("clearBtn");
const historyTable = document.getElementById("historyTable");
const refreshBtn = document.getElementById("refreshBtn");

input.addEventListener("input", () => {
  charCount.textContent = input.value.length;
});

clearBtn.addEventListener("click", () => {
  input.value = "";
  charCount.textContent = 0;
});

refreshBtn.addEventListener("click", () => {
  loadHistory();
  checkHealth();
});

analyzeBtn.addEventListener("click", async () => {
  const text = input.value.trim();

  if (!text) {
    alert("Введите текст сообщения");
    return;
  }

  try {
    analyzeBtn.disabled = true;
    analyzeBtn.textContent = "Анализ...";

    const response = await fetch(`${API_URL}/analyze`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    });

    if (!response.ok) {
      throw new Error("Ошибка анализа");
    }

    const data = await response.json();

    const result = {
      text: text,
      label: data.label,
      score: data.probability,
      date: new Date().toLocaleString()
    };

    updateResult(result);
    await loadHistory();

  } catch (error) {
    alert("Не удалось выполнить анализ. Проверь, запущен ли backend.");
    console.error(error);
  } finally {
    analyzeBtn.disabled = false;
    analyzeBtn.textContent = "Анализировать";
  }
});

async function loadHistory() {
  try {
    const response = await fetch(`${API_URL}/history`);

    if (!response.ok) {
      throw new Error("Ошибка загрузки истории");
    }

    const history = await response.json();
    renderHistory(history);

  } catch (error) {
    console.error("Ошибка истории:", error);
  }
}

function updateResult(result) {
  const labelText = result.label === "SPAM" ? "SPAM" : "NOT SPAM";

  const resultLabel = document.getElementById("resultLabel");
  const resultDesc = document.getElementById("resultDesc");
  const scorePercent = document.getElementById("scorePercent");
  const scoreCircle = document.querySelector(".score-circle");

  const resultCard = document.querySelector(".result-card");

  resultLabel.textContent = labelText;

  resultDesc.textContent =
    result.label === "SPAM"
      ? "Сообщение является спамом"
      : "Сообщение не является спамом";

  scorePercent.textContent =
    Math.round(result.score * 100) + "%";

  document.getElementById("labelValue").textContent = labelText;
  document.getElementById("scoreValue").textContent = result.score;
  document.getElementById("dateValue").textContent = result.date;

if (result.label === "SPAM") {
  resultLabel.style.color = "#ff5f5f";

  scoreCircle.style.borderColor = "#ff5f5f";
  scoreCircle.style.boxShadow = "0 0 18px rgba(255, 95, 95, 0.45)";
  scorePercent.style.color = "#ffffff";

  resultCard.style.borderColor = "#ff5f5f";

} else {
  resultLabel.style.color = "#7CFF9B";

  scoreCircle.style.borderColor = "#7CFF9B";
  scoreCircle.style.boxShadow = "0 0 18px rgba(124, 255, 155, 0.45)";
  scorePercent.style.color = "#ffffff";

  resultCard.style.borderColor = "#7CFF9B";
}
}

function renderHistory(history) {
  historyTable.innerHTML = "";

  history.forEach((item) => {
    const row = `
      <tr>
        <td>${item.id}</td>
        <td>${item.text}</td>
        <td>${item.label}</td>
        <td>${item.probability}</td>
        <td>${new Date(item.created_at).toLocaleString()}</td>
      </tr>
    `;

    historyTable.innerHTML += row;
  });
}

document.addEventListener("DOMContentLoaded", () => {
  checkHealth();
  loadHistory();
});

async function checkHealth() {
  const apiStatusText = document.getElementById("apiStatusText");
  const apiDot = document.getElementById("apiDot");

  const apiMiniStatus = document.getElementById("apiMiniStatus");
  const dbMiniStatus = document.getElementById("dbMiniStatus");
  const modelMiniStatus = document.getElementById("modelMiniStatus");

  try {
    const response = await fetch(`${API_URL}/health`);

    if (!response.ok) {
      throw new Error("API недоступен");
    }

    const data = await response.json();

    apiStatusText.textContent = "Online";
    apiDot.style.backgroundColor = "#7CFF9B";

    apiMiniStatus.textContent = "Работает";
    apiMiniStatus.style.color = "#7CFF9B";

    dbMiniStatus.textContent =
      data.database === "connected" ? "Подключено" : "Ошибка";
    dbMiniStatus.style.color =
      data.database === "connected" ? "#7CFF9B" : "#ff5f5f";

    modelMiniStatus.textContent =
      data.model_loaded ? "Загружена" : "Ошибка";
    modelMiniStatus.style.color =
      data.model_loaded ? "#7CFF9B" : "#ff5f5f";

  } catch (error) {
    apiStatusText.textContent = "Offline";
    apiDot.style.backgroundColor = "#ff5f5f";

    apiMiniStatus.textContent = "Недоступен";
    apiMiniStatus.style.color = "#ff5f5f";

    dbMiniStatus.textContent = "Недоступно";
    dbMiniStatus.style.color = "#ff5f5f";

    modelMiniStatus.textContent = "Недоступна";
    modelMiniStatus.style.color = "#ff5f5f";
  }
}