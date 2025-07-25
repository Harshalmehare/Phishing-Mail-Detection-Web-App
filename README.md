# 📧 PhishGuard – Phishing Email Detector

PhishGuard is a **machine learning web app** that detects phishing emails using **NLP and Naive Bayes**.
It allows users to **paste an email text** and check if it is **phishing 🚨 or safe ✅**.

---

## 📂 Project Files

```
phishing_app/
│── train_model.py     → Train the ML model
│── app.py             → Run the web app
│── model.pkl          → Saved trained model
│── vectorizer.pkl     → Saved TF-IDF vectorizer
│── dataset/
│   └── phishing_email.zip  → Zipped dataset file
│── templates/
│   └── index.html     → Web page design
│── requirements.txt   → Required libraries
│── README.md          → Project details
```

---

## 🛠 How to Run

### 1️⃣ Install Libraries

```bash
pip install -r requirements.txt
```

### 2️⃣ Extract Dataset

```python
import zipfile
with zipfile.ZipFile("dataset/phishing_email.zip", "r") as zip_ref:
    zip_ref.extractall("dataset")
```

### 3️⃣ Train the Model

```bash
python train_model.py
```

### 4️⃣ Start the Web App

```bash
python app.py
```

Then open **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** in your browser.

---

## 🔹 Example Emails

✅ Safe Email → "Meeting tomorrow at 10 AM. Please confirm."
🚨 Phishing Email → "Your account is suspended! Click here to verify."

---

## 🔧 Tech Stack

* Python 3
* Flask
* Scikit-learn
* NLTK

---
