from re import search
from unittest import result
import pyttsx3
import speech_recognition as sr 
import wikipedia
import webbrowser
import pywhatkit
import pyautogui as x




mom = +91888814372

"""voice assistant start here"""
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 200)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.5)    # setting up volume level  between 0 and 1

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

        elif 'search for' in query:
            searchh=query.replace("search for","")
            pywhatkit.search(searchh)

        elif 'nishad status' in query:
            pywhatkit.sendwhatmsg_instantly('+91 88489 94140','where are u now',15,tab_close=True)   
        elif 'banu status' in query:
            pywhatkit.sendwhatmsg_instantly('+91 97455 29102','where are u now',15,tab_close=True)  

        elif 'whatsapp' in query:
            banum=query.replace("whatsapp","")
            pywhatkit.sendwhatmsg_instantly('+91 97455 29102',banum,15,tab_close=True)      

        elif 'open settings' in query:  
            x.hotkey('winleft','i') 

        elif 'close settings' in query:  
            x.hotkey('Alt','F4')     


        elif "sleep" in query:
            spaek ("simba is going offline sir,i will be one call away,thank you for choosing simba 1.0 ")    
              
    

        else :
            speak("can u say it again simba couldn't catch that")
            
        
            

            


