from re import search
from unittest import result
from winsound import PlaySound
import pyttsx3
import speech_recognition as sr 
import wikipedia
import webbrowser
import pywhatkit
import datetime
import pyautogui as x
import playsound

"""voice assistant start here"""
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 200)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',9)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('i am simba 0.1 ajus new AI assistant, i am glad to help you' )
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()

"""speech recoganition"""



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe() :
    hour =int(datetime.datetime.now().hour)
    if hour>=0  and hour<12:
        speak("good morning have a nice day sir")  
    elif hour>=12  and hour<15:   
        speak("good after noon  sir") 
    else:
        speak("good evening")    

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":   
    wishMe() 
    while True:
        query = takeCommand().lower()

        if 'how are you' in query:
            speak("oh i am fine thank you") 
        elif 'how is you' in query:
             speak("hey i am doing good")  
        elif 'i am here' in query :
            speak("glad to meet you")
        elif 'who are you' in query :
            speak("i am simba 0.1 ajus new AI assistant, i am glad to help you")    
        elif 'simba' in query :
            speak("what can i do or you ,sir")  

            """the wekipedia extraction""" 

        elif 'find information about' in query:
            speak('i am finding best results for you')
            query = query.replace("find inormation about","")
            result = wikipedia.summary(query,sentences=2)
            speak("the result is ")
            print(result)
            speak(result)
        elif 'find about' in query:
            speak('i am finding best results for you')
            query = query.replace("find about","")
            result = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia ")
            print(result)
            speak(result)
        elif 'tell about' in query:
            speak('i am finding best results for you')
            query = query.replace("tell about","")
            result = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia ")
            print(result)
            speak(result)  
        elif 'what is' in query:
            speak('i am finding best results for you')
            query = query.replace("what is","")
            result = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia ")
            print(result)
            speak(result)  
        elif 'explain' in query:
            speak('i am finding best results for you')
            query = query.replace("explain","")
            result = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia ")
            print(result)
            speak(result)        
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("YouTube.com")   
        elif 'play' in query:
            song=query.replace ('play','') 
            pywhatkit.playonyt(song)  

        elif 'search'  in query:
            searchh=query.replace("search for","")  
            pywhatkit.search(searchh)

        elif 'where are you' in query:
            playsound('Welcome.wav')  


        elif 'chek status nishad' in query: 
            pywhatkit.sendwhatmsg_instantly('+91 7594 884140','where are u now?',10,tab_close=True)  

        elif 'whatsapp' in query: 
            pywhatkit.sendwhatmsg_instantly('+91 7594 884140','where are u now?',10,tab_close=True)    





        elif ("switch desktop right") in query:
            x.hotkey('winleft', 'cntrl', 'right')
        elif ("switch desktop left") in query:
            x.hotkey('winleft', 'cntrl', 'left')
        elif ("task manager") in query:
            x.hotkey('ctrl', 'shift', 'esc')
        elif ("task view") in query:
            x.hotkey('winleft', 'tab')
        elif ("screenshot") in query:
            x.hotkey('winleft', 'prtscr')
        elif ("open settings") in query:
            x.hotkey('winleft', 'i')
        elif ("switch desktop") in query:
            x.hotkey('winleft', 'ctrl', 'd')            
        elif("select all") in query:
            x.hotkey('cntrl', 'a')
        elif("copy") in query:
            x.hotkey('cntrl', 'c')    
        elif("paste") in query:
            x.hotkey('cntrl', 'v')  
        elif("save") in query:
            x.hotkey('cntrl', 's') 
        elif("undo") in query:
            x.hotkey('cntrl', 'z')
        elif("redo") in query:
            x.hotkey('cntrl', 'y')
        elif("cut") in query:
            x.hotkey('cntrl', 'x')       
        elif("switch tab") in query:
            x.hotkey('alt', 'tab')
        elif("clipboard") in query:
            x.hotkey('winleft', 'v')
        elif("taskbar") in query:
            x.hotkey('winleft', 't')
        elif("maximize") in query:
            x.hotkey('winleft', 'up')
        elif("minimise") in query:
            x.hotkey('winleft', 'down')           
        elif("emoji") in query:
            x.hotkey('winleft', ';') 
        elif("lock") in query:
            x.hotkey('winleft', 'l')
        elif("mute") in query:
            x.hotkey('volumemute')        

        else :
            speak("can u say it again simba couldn't catch that")
            
        
            

            


