import speech_recognition as sr
import pyttsx3
import pywhatkit                   #access youtube
import datetime
import wikipedia
import pyjokes
from googlesearch import search
import re
import time as my_custom_time

import sys
sys.stdout.reconfigure(encoding='utf-8')



listener=sr.Recognizer()
engine=pyttsx3.init()

# voices=engine.getProperty('voices')              # converts to female voice
# engine.setProperty('voice',voices[1].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
                

    except:
        pass
    return command

def runAlexa():
    while True:
        command=takeCommand()
        print(command)

        if 'bye' in command:
            talk("Goodbye!")
            break
        if 'play' in command:
            song= command.replace('play','')
            talk('playing'+ song)
            pywhatkit.playonyt(song)  
        elif 'time' in command: 
            time=datetime.datetime.now().strftime('%I:%M %p')
            print (time)
            talk('current time is' + time)

        elif any(keyword in command for keyword in ['who is','find', 'tell me about', 'what', 'meaning', 'how', 'whom', 'when', 'where']):
            try:
                # Use the entire command as the search term
                info = wikipedia.summary(command, 2)
                print(info)
                talk(info)
            except wikipedia.exceptions.DisambiguationError as e:
                # Handle disambiguation errors (multiple matching results)
                print("Wikipedia disambiguation error:", e.options)
                talk("I found multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                # Handle page not found errors
                print("Wikipedia page error:", e)
                talk("I couldn't find information on that topic.")

        elif 'joke 'in command:
            talk(pyjokes.get_joke()) 

        elif 'google' in command:
            # Extracting the relevant part for the search
            search_query = re.sub(r'google|search', '', command, flags=re.IGNORECASE).strip()
            
            # Performing the Google search
            talk(f"Searching Google for: {search_query}")
            try:
                results = search(search_query)
                for result in results:
                    print(result)
                    my_custom_time.sleep(2)  # Introduce a delay of 2 seconds between requests
                    break  # Break after the first result
            except StopIteration:
                print("No results found.") 
        
        
        else:
            talk("sorry; can you please repeat that")

talk("hi what's up;what can i do for you")
# runAlexa()         
