
# 📰 AI News Summarizer & Q&A Tool 🚀

This project is a **Streamlit-based AI tool** that:
- Summarizes any news article in **3–4 clear sentences**  
- Generates summaries at different **creativity levels** (temperature = 0.1 / 0.7 / 1.0)  
- Lets you **ask questions** about the article and provides answers  
- Shows the **word count** of the article  

---

## 📌 Features
✅ Summarizes news articles quickly  
✅ Multiple summaries at different temperatures  
✅ Q&A section – ask your own questions about the article  
✅ Ignores unrelated questions  
✅ Word count shown  

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/AI-News-Summarizer.git
   cd AI-News-Summarizer
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Linux/Mac
   .venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Setup API Key

1. Create a `.env` file in the root of the project.
2. Add your Google Gemini API key:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

⚠️ **Note:** `.env` is already ignored in `.gitignore` (never upload it to GitHub).

---

## ▶️ Run the App

```bash
streamlit run summarizer.py
```

Then open the link shown in terminal (usually `http://localhost:8501`) in your browser.

---

## 📂 Project Structure

```
.
├── summarizer.py      # Main Streamlit app
├── observations.md    # Example outputs & observations
├── requirements.txt   # Dependencies
├── .env               # API key (ignored by git)
├── .gitignore         # Ignore rules
└── README.md          # Project documentation
```

---

## 📝 Example Output

### Summaries at Different Temperatures

* **0.1:** Very precise and factual  
* **0.7:** Balanced, slight creativity  
* **1.0:** More diverse and creative wording  

### Q&A

* ❓ Why was the operation held?  
* ❓ Where was it held?  
* ❓ How many terrorists were killed?  

---

## 🤝 Contributing

Pull requests are welcome!  

---

## 📜 License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute this software with attribution.
````

