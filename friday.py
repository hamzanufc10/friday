import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import ctypes
import random
import json


speech=sr.Recognizer()

soc = {'Facebook': 'https://www.facebook.com/', 'Google': 'https://www.instagram.com/accounts/login/'}
google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which', 'is': 'is'}

try:
    engine = pyttsx3.init()
except ImportError:
    print('request driver not found')
except RuntimeError:
    print('driver fails to init')


voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id)

engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
rate=engine.getProperty('rate')
engine.setProperty('rate',rate)


#engine.say('Hello Sir,this is Alfred')
#engine.runAndWait()





def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    voice_text =''
    print("listining...")
    with sr.Microphone() as source:
        audio=speech.listen(source=source,timeout=8,phrase_time_limit=5)
    try:
        voice_text=speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('Network error')
    return voice_text





def is_valid_google_search(phrase):
    if (google_searches_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]):
        return True


if __name__ == '__main__':
    speak_text_cmd('Hello Master hamza.....Alfred on your service')

    while True:


            voice_note = read_voice_cmd().lower()
            print('cmd : {}'.format(voice_note))
            if 'hello alfred' in voice_note:
                speak_text_cmd("Hello Master shakeel....how can i help you ?")
                continue
            elif 'open windows' in voice_note:
                speak_text_cmd("ok sir")
                os.system('explorer C:\\ {}'.format(voice_note))
                continue

            elif 'lock' in voice_note:
                for values in ['my system',' my windows','my pc']:
                    speak_text_cmd("ok sir......your system is being locked")
                    ctypes.windll.user32.LockWorkStation()
                    exit()

                    break
            elif 'youtube' in voice_note:
                speak_text_cmd("as you wish sir")
                webbrowser.open('https://www.youtube.com/')
                continue

            elif 'facebook' in voice_note:
                speak_text_cmd("as you wish sir")
                webbrowser.open('https://www.facebook.com/')

                continue
            elif 'close it' in voice_note:
                speak_text_cmd("as you wish sir")
                os.system("taskkill /im chrome.exe /f")
                continue
            elif 'instagram' in voice_note:
                speak_text_cmd("as you wish sir")
                webbrowser.open('https://www.instagram.com/accounts/login/')
                continue

            elif is_valid_google_search(voice_note):
                speak_text_cmd("Finding sir")
                webbrowser.open('https://www.google.com/search?q={}'.format(voice_note))
                continue
            elif 'by' in voice_note:
                speak_text_cmd('Bye sir...happy to help you.....have a good day')
                exit()















