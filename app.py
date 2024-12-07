!pip install gradio transformers

import gradio as gr
from transformers import pipeline
import json

# Load the sentiment analysis model
sentiment_model = pipeline("sentiment-analysis")

# Define yoga recommendation logic
def get_yoga_recommendation(mood):
    sentiment_result = sentiment_model(mood)[0]
    sentiment = sentiment_result["label"].lower()
    confidence = sentiment_result["score"]

    recommendations = {
        "positive": {
            "routine": "Hatha Yoga: Focus on grounding and stretching poses.",
            "advice": "Take this session as an opportunity to try new challenging poses!"
        },
        "neutral": {
            "routine": "Yin Yoga: Slow and meditative poses to help you unwind.",
            "advice": "Focus on your breathing and let your thoughts flow naturally."
        },
        "negative": {
            "routine": "Restorative Yoga: Gentle and calming poses to release stress.",
            "advice": "Take it easy, listen to your body, and focus on relaxation."
        },
    }

    recommendation = recommendations.get(
        sentiment,
        {"routine": "Meditation", "advice": "Practice deep breathing to calm your mind."}
    )

    # Return recommendation details along with sentiment and confidence score
    return {
        "Sentiment": sentiment.capitalize(),
        "Confidence": f"{confidence:.2f}",
        "Yoga Routine": recommendation["routine"],
        "Advice": recommendation["advice"]
    }

# Gradio interface
def analyze_mood(mood):
    recommendation = get_yoga_recommendation(mood)

    # Save the result to a file (appending to log)
    with open("gradio_log.json", "a") as log_file:
        log_file.write(json.dumps(recommendation) + "\n")

    # Display the recommendation results
    return f"""
    Sentiment: {recommendation['Sentiment']}
    Confidence: {recommendation['Confidence']}
    Yoga Routine: {recommendation['Yoga Routine']}
    Advice: {recommendation['Advice']}
    """

# Create Gradio app
gr.Interface(
    fn=analyze_mood,
    inputs="text",
    outputs="text",
    title="Yoga Recommendation System",
    description="Enter your mood, and get a personalized yoga routine!"
).launch()
