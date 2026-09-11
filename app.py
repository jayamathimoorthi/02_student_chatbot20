from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

BOT_NAME = os.environ.get("BOT_NAME", 'Student Helper')
BOT_DESCRIPTION = os.environ.get("BOT_DESCRIPTION", 'Helps students with study planning and explanations.')

def reply(message):
    text = message.lower().strip()
    if not text:
        return "Please type a message."
    if any(x in text for x in ["hello", "hi", "hey"]):
        return f"Hello! I'm {BOT_NAME}. How can I help you?"
    if "help" in text:
        return f"I can help with {BOT_DESCRIPTION.lower()}"
    if any(x in text for x in ["bye", "goodbye"]):
        return "Goodbye! Have a great day."
    return f"You said: {message}\n\nI'm a demo chatbot. Connect this reply() function to your AI API to make me fully AI-powered."

@app.route("/")
def home():
    return render_template("index.html", bot_name=BOT_NAME, description=BOT_DESCRIPTION)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    return jsonify({"reply": reply(data.get("message", ""))})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
