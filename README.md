# Yoga Recommendation System Using Sentiment Analysis

## Project Overview

This project leverages **sentiment analysis** to recommend personalized yoga routines based on the user's mood. The system uses a pre-trained sentiment analysis model from Hugging Face to classify the mood of the user and then maps that mood to an appropriate yoga routine.

The app is implemented in **Python** using **Gradio** for the interface and **Transformers** from Hugging Face for the sentiment analysis model.

## Approach

### **1. Sentiment Analysis**
- The model analyzes a user's input (text) and classifies the sentiment into **positive**, **neutral**, or **negative**.
- Based on the sentiment, the system recommends a corresponding yoga routine.

### **2. Yoga Routine Mapping**
- **Positive Sentiment**: Recommends "Hatha Yoga" for grounding and stretching.
- **Neutral Sentiment**: Recommends "Yin Yoga" for slow-paced movements.
- **Negative Sentiment**: Recommends "Restorative Yoga" to release stress and tension.
- If the sentiment is unknown, **Meditation** is recommended.

### **3. Logging**
- Each user’s input and corresponding recommendation are logged into a file called `gradio_log.json`. This allows for tracking and analyzing the system's usage.

## Data Preprocessing
- The project does not require any custom dataset. Instead, we leverage a pre-trained sentiment analysis model (`distilbert-base-uncased-finetuned-sst-2-english`) from the **Hugging Face model hub**.
  
## Model Architecture
- The project uses the **DistilBERT** model, which is a smaller, faster, and cheaper version of BERT, fine-tuned for sentiment analysis.
- The model provides a **positive**, **neutral**, or **negative** sentiment score, which is then mapped to a yoga recommendation.

## Results

The system works by accepting text input from the user, performing sentiment analysis on the input, and providing a yoga recommendation based on the sentiment classification. 

The user receives:
- Sentiment analysis result (Positive/Neutral/Negative)
- Yoga routine recommendation
- Helpful advice for performing the recommended routine

## Next Steps
1. **Enhance User Input**: Add support for voice or image input to detect mood via speech or facial expressions.
2. **Deploy the System**: Deploy the app on cloud platforms such as **Heroku** or **Render** for public access.
3. **Integration with Wearables**: Integrate with wearable devices (like a fitness tracker) to suggest routines based on real-time data.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Yoga-Recommendation-System.git
