import speech_recognition as sr
import time
import random
from gtts import gTTS
import os

readyToGo = ['Oui ?', 'Qu\'y a-t\'il ?', 'Quoi encore ?']
language = 'fr-FR'

def transcribe_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language=language)
    except:
        print('Don\'t work')

def getMacMicro():
    liste = sr.Microphone.list_microphone_names()
    return liste.index('MacBook Pro Microphone')

def speak_text(text):
    myobj = gTTS(text=text, lang='fr', slow=False)
    myobj.save('current.mp3')
    os.system("afplay current.mp3")
    
# class Fonction:
    

def main():
    while True :
        print('Listenning...')
        with sr.Microphone(device_index=getMacMicro()) as source:
            reconizer = sr.Recognizer()
            audio = reconizer.listen(source)
        try :
            transcription = reconizer.recognize_google(audio, language=language)
            # print(f"Transcritpion :\n{transcription}")

            if transcription.lower() == 'jarvis':
                filename = 'listen.wav'
                speak_text(random.choice(readyToGo))
                
                with sr.Microphone(device_index=getMacMicro()) as source:
                    reconizer = sr.Recognizer()
                    source.pause_treshold = 1
                    audio = reconizer.listen(source, phrase_time_limit=None, timeout=None)
                    
                    with open(filename, 'wb') as f:
                        f.write(audio.get_wav_data())
                    
                text = transcribe_to_text(filename)
                if text:
                    print(f'You said : {text}')
                    speak_text('Oui et vous ?')

            if transcription.lower() == 'exit':
                exit()

        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()