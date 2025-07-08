task-1
🌐 Smart Language Translator
A feature-rich GUI application built with Python and Tkinter that allows users to translate text between over 100 languages. It supports voice input, text-to-speech, and a dark mode toggle for enhanced usability.

🚀 Features
🔄 Instant translation between multiple languages using Google Translate
🎤 Voice Input: Speak your sentence directly into the microphone
🔊 Text-to-Speech: Listen to the translated output
🌗 Light/Dark Mode toggle for better UI experience
🪟 Clean, responsive GUI using Tkinter
🌐 Supports over 100+ languages
📝 Intuitive text input with editable fields
📋 Copy translated text easily for use elsewhere

🛑 Input validation and error handling (e.g., no input, network errors)

📸 GUI Preview
Add a screenshot of your app here (optional)

🛠️ Requirements
Install the dependencies before running the app: pip install googletrans==4.0.0-rc1 pyttsx3 SpeechRecognition pyaudio
pip install pipwin
pipwin install pyaudio
💡 How to Use

Select your source and target languages.
Enter text manually or use the 🎤 Speak button.
Click Translate to get the translation.
Use 🔊 Read Aloud to hear the result.
Toggle between Dark/Light mode as desired.

📚 Technologies Used
Python 3.x
Tkinter
Googletrans
Pyttsx3
SpeechRecognition
Pyaudio

task-2

🤖 FAQ Chatbot using Python and NLP
This is a simple command-line FAQ Chatbot built using Python. It uses NLTK for natural language processing and TF-IDF with cosine similarity to match user questions with the most relevant frequently asked question.

🚀 Features
📖 Preprocesses questions using tokenization, lowercasing, punctuation removal, and stopword filtering
🤝 Matches user queries with closest FAQ using cosine similarity
💬 Returns the most appropriate answer from a custom knowledge base
🖥️ Command-line based — lightweight and fast
🧠 Easy to customize or extend with more Q&A
🗃️ Modular knowledge base stored in dictionary format
⏱️ Simulated thinking delay for natural interaction

📚 Technologies Used
Python 3.x
NLTK
Scikit-learn
Tkinter (for GUI version if extended)
Threading (for non-blocking GUI interactions)
TF-IDF Vectorizer (for query matching)

