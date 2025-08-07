# 🧠 Emotion Detection from Text (Streamlit App)

This is a simple and powerful Streamlit web app that detects the emotion expressed in a given piece of text using a trained deep learning model.

## 🔗 Live App

👉 [Click here to use the live app](https://daya-2619-emotion-detection-app-sokkqg.streamlit.app/)

---

## 📌 Features

- Detects emotions from raw text input
- Deep learning model (BiLSTM + Embedding)
- Preprocessing pipeline with Tokenizer and LabelEncoder
- Deployed using Streamlit Cloud
- Supports common emotions like **joy**, **anger**, **fear**, **sadness**, **surprise**, and **love**

---

## 🛠 Tech Stack

- Python
- TensorFlow / Keras
- Scikit-learn
- Streamlit
- Joblib
- Pandas / NumPy / Matplotlib

---

## 📦 Project Structure

```
emotion-detection-app/
├── app.py                  # Main Streamlit app
├── emotion_model.h5        # Trained LSTM model
├── tokenizer.jb            # Tokenizer for text preprocessing
├── label_encoder.jb        # Label encoder for emotion labels
├── requirements.txt        # All required Python packages
└── runtime.txt             # Python version for Streamlit Cloud
```

---

## 🚀 How to Run Locally

1. **Clone this repo**

   ```bash
   git clone https://github.com/daya-2619/emotion-detection.git
   cd emotion-detection-app
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

---

## 📷 Screenshot

<img width="1346" height="567" alt="Screenshot 2025-08-07 132443" src="https://github.com/user-attachments/assets/b3452cec-c3b6-4d88-92db-8788f756789a" />


---

## 📮 Contact

Feel free to reach out on [LinkedIn](https://www.linkedin.com/in/dayamay-das-036466351/) or create an issue on this repo.

---

## ⭐️ Give a Star

If you found this project helpful, please consider giving it a ⭐️ on GitHub!
