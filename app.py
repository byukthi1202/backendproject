from flask import Flask, request, jsonify
from flask_cors import CORS
import language_tool_python

app = Flask(__name__)
CORS(app)

tool = language_tool_python.LanguageTool('en-US')

@app.route("/check-grammar", methods=["POST"])
def check_grammar():
    data = request.get_json()
    text = data.get("text", "")

    matches = tool.check(text)
    corrected = language_tool_python.utils.correct(text, matches)

    return jsonify({
        "corrected_text": corrected
    })

if __name__ == "__main__":
    app.run()
