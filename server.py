"""Flask server for the emotion detection application."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the text provided by the user and return emotion results."""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and "
        "'sadness': {}. The dominant emotion is {}.".format(
            response["anger"],
            response["disgust"],
            response["fear"],
            response["joy"],
            response["sadness"],
            response["dominant_emotion"],
        )
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)