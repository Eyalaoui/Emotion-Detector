# Emotion Detection Web Application

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v2.0+-green.svg)
![IBM Watson](https://img.shields.io/badge/IBM-Watson-blue.svg)

A web-based emotion detection application built with Flask and IBM Watson AI libraries. This project was developed as the final project for the IBM certification course "Developing AI Applications with Python and Flask".

## 📋 Project Overview

This application analyzes text input and detects emotions using IBM Watson's Natural Language Processing capabilities. It identifies five primary emotions (anger, disgust, fear, joy, sadness) and determines the dominant emotion in the given text.

## 🚀 Features

- **Real-time Emotion Analysis**: Analyze text and get instant emotion detection results
- **Multi-emotion Detection**: Identifies anger, disgust, fear, joy, and sadness with confidence scores
- **Dominant Emotion Identification**: Determines the primary emotion in the text
- **Web Interface**: User-friendly web interface for easy interaction
- **Error Handling**: Robust error handling for invalid inputs
- **REST API**: RESTful endpoint for programmatic access

## 🛠️ Technologies Used

- **Python 3.7+**: Core programming language
- **Flask**: Web framework for creating the web application
- **IBM Watson NLP**: AI libraries for emotion detection
- **HTML/CSS**: Frontend user interface
- **unittest**: Testing framework

## 📁 Project Structure

```
emotion-detection/
│
├── EmotionDetection/           # Main package directory
│   └── emotion_detection.py    # Core emotion detection logic
│
├── templates/                  # HTML templates
│   └── index.html             # Main web interface
│
├── static/                     # Static files (CSS, JS, images)
│
├── server.py                   # Flask web server
├── test_emotion_detection.py   # Unit tests
├── README.md                   # Project documentation
└── LICENSE                     # License file
```

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/emotion-detection.git
   cd emotion-detection
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv emotion_env
   source emotion_env/bin/activate  # On Windows: emotion_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   pip install requests
   # Additional Watson AI libraries as required
   ```

4. **Run the application**
   ```bash
   python server.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5001`

## 🎯 Usage

### Web Interface
1. Navigate to the main page at `http://localhost:5001`
2. Enter your text in the input field
3. Click "Analyze Emotion" to get results
4. View the emotion scores and dominant emotion

### API Endpoint
```bash
curl "http://localhost:5001/emotionDetector?textToAnalyze=I am so happy today"
```

**Response Format:**
```
For the given statement, the system response is 'anger': 0.02, 'disgust': 0.01, 'fear': 0.03, 'joy': 0.89 and 'sadness': 0.05. The dominant emotion is joy.
```

## 🧪 Testing

Run the unit tests to verify the application functionality:

```bash
python test_emotion_detection.py
```

The test suite covers:
- Joy detection: "I am glad this happened"
- Anger detection: "I am really mad about this"
- Disgust detection: "I feel disgusted just hearing about this"
- Sadness detection: "I am so sad about this"
- Fear detection: "I am really afraid that this will happen"

## 🏗️ Development Process

This project followed the standard AI application development lifecycle:

1. **Function Creation**: Developed the core emotion detection function
2. **Package Development**: Organized code into a proper Python package
3. **Unit Testing**: Implemented comprehensive tests for all emotion types
4. **Web Deployment**: Created Flask web application with REST API
5. **Error Handling**: Added robust error handling for edge cases
6. **Code Analysis**: Performed static code analysis for code quality

## 🔍 Error Handling

The application includes comprehensive error handling:

- **Empty Input**: Returns "Invalid text! Please try again!" for empty or whitespace-only input
- **Invalid Response**: Handles cases where the AI service returns None for dominant emotion
- **Service Errors**: Graceful handling of Watson AI service failures

## 📊 Emotion Categories

The application detects five primary emotions:

| Emotion | Description |
|---------|-------------|
| **Joy** | Happiness, contentment, satisfaction |
| **Anger** | Frustration, irritation, rage |
| **Sadness** | Sorrow, melancholy, disappointment |
| **Fear** | Anxiety, worry, apprehension |
| **Disgust** | Revulsion, distaste, aversion |

## 🎓 Educational Context

This project was developed as part of the IBM certification course "Developing AI Applications with Python and Flask". It demonstrates:

- Integration of Watson AI libraries in web applications
- RESTful API development with Flask
- Test-driven development practices
- Error handling in AI applications
- Deployment of AI-powered web services



**Note**: This application uses IBM Watson AI libraries which may require proper authentication and setup for full functionality. Please refer to IBM Watson documentation for API key configuration.
