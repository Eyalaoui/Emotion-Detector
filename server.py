"""Flask server for the Emotion Detector web application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("emotion detector")
@app.route("/emotionDetector")
def emo_detector():
    """Handles the /emotionDetector endpoint and returns the emotion analysis result."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
     # Error handling if dominant_emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    output = (
    f"For the given statement, the system response is "
    f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
    f"'fear': {response['fear']}, 'joy': {response['joy']} and "
    f"'sadness': {response['sadness']}. "
    f"The dominant emotion is {response['dominant_emotion']}."
)
    return output
@app.route("/")
def render_index_page():
    """Renders the index HTML page."""
    return render_template('index.html')

2
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)