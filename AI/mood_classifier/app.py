from textblob import TextBlob
import emoji
import speech_recognition as sr
import pyttsx3
import time

# Initialize text-to-speech engine
tts = pyttsx3.init()

# Set voice to female
voices = tts.getProperty('voices')
for voice in voices:
    if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
        tts.setProperty('voice', voice.id)
        break  # use the first matching female voice

# Function to speak
def speak(text):
    tts.say(text)
    tts.runAndWait()

# Analyze sentiment
def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.3:
        mood = "Happy"
        symbol = "😄"
    elif polarity < -0.3:
        mood = "Sad"
        symbol = "😢"
    else:
        mood = "Neutral"
        symbol = "😐"

    result = f"Polarity Score: {polarity:.2f} → Mood: {mood} {symbol}"
    speak(f"You said: {text}")
    speak(f"You sound {mood.lower()}")
    return result

# Listen to speech
def listen_to_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🟡 Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("🎤 Speak now! I'm listening...")
        time.sleep(0.3)
        audio = recognizer.listen(source)
        print("⏳ Got it! Processing...\n")

        try:
            text = recognizer.recognize_sphinx(audio)
            print(f"🗣️ You said: {text}")
            return text
        except sr.UnknownValueError:
            print("❗ Sorry, I could not understand the audio.")
            speak("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print(f"❗ Sphinx error: {e}")
            speak("There was a problem with the speech recognition.")
        return None

# Main app
def run_app():
    print("🎉 Welcome to the OFFLINE AI-Powered Emoji Mood Classifier with Voice!")
    print("Speak something, and I'll tell you your mood with an emoji and repeat what you said.")
    print("Say 'exit' to quit.\n")
    speak("Welcome! I will guess your mood. Say something!")

    while True:
        sentence = listen_to_speech()
        if sentence is None:
            continue
        if sentence.lower() in ['exit', 'quit']:
            speak("Goodbye! Stay positive!")
            print("👋 Goodbye! Stay positive!")
            break
        result = analyze_mood(sentence)
        print(result + "\n")

if __name__ == "__main__":
    run_app()
