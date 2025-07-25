from flask import Flask, request, render_template
import pickle, re, nltk

nltk.download("stopwords")
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    text = re.sub(r"http\S+", "", str(text))
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower()
    words = [w for w in text.split() if w not in stop_words]
    return " ".join(words)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        email_text = request.form["email_text"]
        cleaned = clean_text(email_text)
        vectorized = vectorizer.transform([cleaned])
        pred = model.predict(vectorized)[0]
        result = "🚨 Phishing Email" if pred == 1 else "✅ Safe Email"
    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
