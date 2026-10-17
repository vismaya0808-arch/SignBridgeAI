
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

SIGN_LIBRARY = {
    "open your textbook": "open_textbook.mp4",
    "write the answer": "write_answer.mp4",
    "look at the board": "look_board.mp4",
    "any questions": "questions.mp4",
    "please repeat": "repeat.mp4"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    sentence = data.get("text", "").lower().strip()

    # Match the supported phrase inside a longer sentence
    video = None

    for phrase, filename in SIGN_LIBRARY.items():
        if phrase in sentence:
            video = filename
            break

    return jsonify({
        "text": sentence,
        "video": video,
        "supported": video is not None
    })

if __name__ == "__main__":
    app.run(debug=True)
