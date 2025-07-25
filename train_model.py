import pandas as pd
import re, pickle, nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# ✅ Download stopwords
nltk.download("stopwords")
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))

# ✅ Load dataset
df = pd.read_csv(r"dataset\phishing_email.csv")
df.rename(columns={'text_combined': 'text'}, inplace=True)

print("✅ Columns in Dataset:", df.columns)
print(df.head())

# ✅ Remove rows where label is missing
df = df.dropna(subset=["label"])

# ✅ Ensure label is integer
df["label"] = df["label"].astype(int)

print("✅ Unique labels after cleaning:", df["label"].unique())

# ✅ Clean text function
def clean_text(text):
    text = re.sub(r"http\S+", "", str(text))
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower()
    words = [w for w in text.split() if w not in stop_words]
    return " ".join(words)

df["clean_text"] = df["text"].apply(clean_text)

# ✅ TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["clean_text"])
y = df["label"]

# ✅ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train Model
model = MultinomialNB()
model.fit(X_train, y_train)

# ✅ Evaluate Model
y_pred = model.predict(X_test)
print("\n✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n✅ Classification Report:\n", classification_report(y_test, y_pred))

# ✅ Save Model and Vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
print("\n✅ Model and Vectorizer Saved!")
