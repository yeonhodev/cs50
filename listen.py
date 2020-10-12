import speech_recognition
import pyttsx3

engine = pyttsx3.init()

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something: ")
    audio = recognizer.listen(source)

print("You said:")
print(recognizer.recognize_google(audio))

words = recognizer.recognize_google(audio)

if "hello" in words:
    print("Hello to you too!")
    engine.say("Hello to you too!")
    engine.runAndWait()
elif "how are you" in words:
    print("I am well, thanks!")
    engine.say("I am well, thanks!")
    engine.runAndWait()
elif "prettiest" in words:
    print("It's definitely Carol!")
    engine.say("It's definitely Carol!")
    engine.runAndWait()
elif "goodbye" in words:
    print("Goodbye to you too!")
    engine.say("Goodbye to you too!")
    engine.runAndWait()
else:
    print("Huh?")