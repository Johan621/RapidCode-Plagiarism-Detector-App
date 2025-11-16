### **🛡️ Rapid Code Plagiarism Detector**

NLP • ML • Streamlit • Automatic Typing-Time Cheating Detection

This project detects plagiarism in coding assignments using TF-IDF similarity and detects cheating behaviors using real-time typing speed analysis — all inside a clean Streamlit UI.

### **🚀 Features**

**🔍 1. Code Similarity Detection**

Uses TF-IDF (Scikit-learn)

Cosine Similarity

Detects copy-paste, paraphrased, and slightly modified code

Color-coded plagiarism score

**⏱️ 2. Typing-Time Cheating Detector (Unique Feature)**

Automatically detects if students:

Actually typed their code line-by-line

Pasted large chunks instantly

Typing too fast for any human to achieve

Uses keystroke timing to catch unfair practices in online contests or assignment submissions.

**🧠 Tech Stack**

Streamlit — UI

Scikit-learn — TF-IDF + ML

NLTK — Tokenization

Python — typing-time analysis


### **📁 Project Structure**

Rapid-code-plagiarism-tool/
│── app.py
│── README.md
│── requirements.txt
│── utils/
│     ├── similarity.py
│     ├── typing_detector.py
│     ├── datapreprocessing.py


### **▶️ Run Locally**
```bash
pip install -r requirements.txt
streamlit run app.py
```
### **🌐 Deploy on Streamlit Cloud**

```bash
Push this repository to GitHub

Go to https://share.streamlit.io

Connect your repo

Select app.py

Deploy 🚀

```

### **💡 Why This Project Is Unique**

Combines NLP + ML + Streamlit

Detects copy-paste cheating in coding contests/exams

Real-time keytype analysis without external libraries
