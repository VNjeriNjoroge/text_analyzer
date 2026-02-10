import streamlit as st
from textblob import TextBlob

# Page configuration
st.set_page_config(page_title="Sentiment Analyzer", page_icon="😊")

def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Polarity ranges from -1 (Negative) to 1 (Positive)
    return analysis.sentiment.polarity

st.title("Simple Sentiment Analyzer")
st.write("Enter text below to determine if the sentiment is Positive, Negative, or Neutral.")

# User input
user_input = st.text_area("Enter your message:", placeholder="Type here...")

if st.button("Analyze"):
    if user_input.strip():
        score = analyze_sentiment(user_input)
        
        # Display results
        if score > 0:
            st.success(f"Positive Sentiment (Score: {score:.2f})")
        elif score < 0:
            st.error(f"Negative Sentiment (Score: {score:.2f})")
        else:
            st.info(f"Neutral Sentiment (Score: {score:.2f})")
    else:
        st.warning("Please enter some text first.")
