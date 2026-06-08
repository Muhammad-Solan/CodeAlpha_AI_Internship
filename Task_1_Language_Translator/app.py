from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Hindi": "hi",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Russian": "ru",
    "Turkish": "tr",
    "Italian": "it",
    "Portuguese": "pt"
}

@app.route("/", methods=["GET", "POST"])
def home():

    translated_text = ""

    if request.method == "POST":

        text = request.form["text"]
        source = request.form["source"]
        target = request.form["target"]

        try:
            translated_text = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

        except Exception:
            translated_text = "Translation failed. Please try again."

    return render_template(
        "index.html",
        languages=languages.keys(),
        translated_text=translated_text
    )

if __name__ == "__main__":
    app.run(debug=True)