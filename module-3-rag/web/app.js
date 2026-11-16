"use strict";

const form = document.querySelector("#question-form");
const question = document.querySelector("#question");
const submit = document.querySelector("#submit");
const results = document.querySelector("#results");
const activity = document.querySelector("#activity");

function make(tag, text, className) {
  const node = document.createElement(tag);
  node.textContent = text;
  if (className) node.className = className;
  return node;
}

function renderResult(result) {
  const status = document.querySelector("#answer-status");
  status.dataset.state = result.status;
  status.textContent = result.status === "answered" ? "Answered from sources" : "Insufficient evidence";
  document.querySelector("#answer-text").textContent = result.answer;

  const citations = document.querySelector("#citations-list");
  const sources = document.querySelector("#sources");
  citations.replaceChildren();
  sources.replaceChildren();
  for (const source of result.sources) {
    const detail = make("details", "", "source");
    detail.id = `source-${source.id}`;
    detail.append(
      make("summary", `${source.id} · ${source.title}`),
      make("p", `Audience: ${source.audience} · Effective ${source.effective}`, "source-meta"),
      make("p", source.text)
    );
    const citation = make("a", source.id, "citation");
    citation.href = `#${detail.id}`;
    citation.addEventListener("click", () => { detail.open = true; });
    citations.append(citation);
    sources.append(detail);
  }

  document.querySelector("#search-metrics").textContent =
    `Cosine similarity · ${result.metrics.search_ms} ms retrieval · ${result.metrics.total_ms} ms total`;
  const matches = document.querySelector("#matches");
  matches.replaceChildren();
  for (const match of result.retrieved) {
    const item = make("li", "");
    item.append(
      make("span", `${match.id} · ${match.title}`),
      make("span", `${match.similarity.toFixed(3)} · ${match.in_context ? "sent to model" : "below cutoff"}`, "match-info")
    );
    matches.append(item);
  }
  results.hidden = false;
  activity.textContent = result.status === "answered" ? "Answer is ready." : "No supported answer found.";
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const value = question.value.trim();
  if (!value || submit.disabled) return;
  submit.disabled = true;
  results.hidden = true;
  activity.textContent = "Searching the handbook…";
  try {
    const response = await fetch("/api/ask", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({question: value})
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "The local server could not answer.");
    renderResult(data);
  } catch (error) {
    activity.textContent = error.message;
  } finally {
    submit.disabled = false;
  }
});

for (const button of document.querySelectorAll("[data-question]")) {
  button.addEventListener("click", () => {
    if (submit.disabled) return;
    question.value = button.dataset.question;
    form.requestSubmit();
  });
}
