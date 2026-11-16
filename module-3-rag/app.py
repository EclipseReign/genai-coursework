"""Loopback web interface for Canal Works."""

import sqlite3

from flask import Flask, jsonify, request

from rag import RagError, ask

app = Flask(__name__, static_folder="web", static_url_path="/assets")
app.config["MAX_CONTENT_LENGTH"] = 4096


@app.get("/")
def home():
    return app.send_static_file("index.html")


@app.post("/api/ask")
def answer_question():
    data = request.get_json(silent=True)
    question = data.get("question") if isinstance(data, dict) else None
    if not isinstance(question, str):
        return jsonify(error="Send a question as text."), 400
    try:
        return jsonify(ask(question))
    except ValueError as error:
        return jsonify(error=str(error)), 400
    except RagError as error:
        return jsonify(error=str(error)), 503
    except sqlite3.Error:
        app.logger.exception("Cannot read the handbook index")
        return jsonify(error="Cannot read the handbook index. Run python rag.py ingest."), 503


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
