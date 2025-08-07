import streamlit as st 
import joblib as jb
import tensorflow as tf 
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re 
import numpy as np


model = tf.keras.models.load_model("emotion_model.h5")

tokenizer = jb.load("tokenizer.jb")
label_encoder = jb.load("label_encoder.jb")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\S+", "", text)
    text = re.sub(r"@\W+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()  # normalize spaces, don't remove them completely
    return text


def predictor(text):
    processed_text = preprocess_text(text)
    sequence = tokenizer.texts_to_sequences([processed_text])
    padded_sequence = pad_sequences(sequence, maxlen=100 ,padding = "post")
    prediction = model.predict(padded_sequence)
    predicted_label = label_encoder.inverse_transform([np.argmax(prediction)])
    return predicted_label
st.title("emotion-detection")
st.write("Enter the text to detect emotion")

user_input = st.text_area("Input Text")
if st.button("Predict"):
    if user_input:
        prediction = predictor(user_input)
        st.write(f"Predicted Emotion: {prediction}")
    else:
        st.error("Please enter some text to predict emotion.")