import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")
for voice in voices:
    print(voice.name)
    engine.setProperty('voice', voice.id)
    engine.say("Bonjour, comment allez-vous ?")
    engine.runAndWait()