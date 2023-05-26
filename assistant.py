import pvporcupine
from pvrecorder import PvRecorder
import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
from pydub.playback import play
import os
import pvleopard

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, Language='en-in') 
        print(f"User said: {query}\n")  
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query =  takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'D:\\Users\\COMPAC\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.starfile(os.path.join(music_dir, songs[0]))
            

            pass

access_key = "PIZlZJPGRmtG+ZqSBQNHdgObhykHhjdqle2t92fwecEVQQokvSElXQ=="
keywords = ["alexa", "americano", "blueberry", "bumblebee", "grapefruit", "grasshopper", "hey google", "hey siri", "jarvis", "ok google", "picovoice", "porcupine", "terminator"]
porcupine = pvporcupine.create(access_key=access_key, keywords=keywords)
recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

def visualize(data):
    # print(data)
    pass

def record_commands(fs=16000, seconds=5, filename='command.wav'):
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, myrecording)
    print('Recording finished')
    return filename

def check_for_commands(words):
    if 'play' in words:
        print('Playing...')
        song = AudioSegment.from_mp3('song.mp3')
        play(song)
        print('Finished playing')

try:
    file = 'command.wav'
    recoder.start()
    print("Listening... (Press Ctrl+C to exit)")
    while True:
        if os.path.exists(file): os.unlink(file)
        recording = recoder.read()
        visualize(recording)
        keyword_index = porcupine.process(recording)
        if keyword_index >= 0:
            print(f"Detected {keywords[keyword_index]}")
            print('Recording...')
            file = record_commands()
        if os.path.exists(file) and os.path.getsize(file) > 0: 
            print('Processing...')
            leopard = pvleopard.create(access_key=access_key)
            transcript, words = leopard.process_file(file)
            if transcript:
                print(f"Transcript: {transcript}")
                if len(words) > 0:
                    check_for_commands(words)
                else:
                    print('No words detected')
            else:
                print('No transcript detected')
            leopard.delete()


except KeyboardInterrupt:
    recoder.stop()
finally:
    porcupine.delete()
    recoder.delete()