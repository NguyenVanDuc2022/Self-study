import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Hello mr.Duc. This is Friday")
