# my original code starts here

import speech_recognition as sr
import pyttsx3
import pywhatkit                                   #access youtube
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
    # try:
    #     with sr.Microphone() as source:
    #         print('listening...')
    #         voice=listener.listen(source)
    #         command=listener.recognize_google(voice)
    #         command=command.lower()
    #         if 'alexa' in command:
    #             command=command.replace('alexa','')
    #             print(command)
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            voice = listener.listen(source, timeout=5)  # Set timeout to 5 seconds
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
            
    except sr.UnknownValueError:
        # Handle case where speech is not recognized
        print("Sorry :( I could not get it...Please repeat")
        command = "Sorry :( I could not get it...Please repeat"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        command = "Sorry :( I encountered an error. Please try again."

    return command
                

    # except:
    #     pass
    # return command

def runAlexa():
    responses = []  # Store responses in a list

    while True:
        command=takeCommand()
        print(command)
        responses.append(f"Command: {command}\n")

        if 'bye' in command:
            print("Goodbye !!")
            talk("Goodbye friend!")
            responses.append("Goodbye!")
            break
        if 'play' in command or 'song'in command or 'songs'in command:
            song= command.replace('play','')
            talk('playing'+ song)
            responses.append(f'Playing {song}\n')
            pywhatkit.playonyt(song)  
        elif 'time' in command: 
            time=datetime.datetime.now().strftime('%I:%M %p')
            print ('current time is',time)
            responses.append(f'Current time is {time}\n')
            sys.stdout.flush()  # Flush the output to ensure real-time updates
            talk('current time is' + time)
        elif 'wikipedia' in command:
            try:
                # Use the entire command as the search term
                info = wikipedia.summary(command, 2)
                print(info)
                responses.append(f"{info}\n")
                talk(info)
            except wikipedia.exceptions.DisambiguationError as e:
                # Handle disambiguation errors (multiple matching results)
                print("Wikipedia disambiguation error:", e.options)
                responses.append(f"Wikipedia disambiguation error: {e.options}\n")
                talk("I found multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                # Handle page not found errors
                print("Wikipedia page error:", e)
                responses.append(f"Wikipedia page error: {e}\n")
                talk("I couldn't find information on that topic.")
        elif 'joke ' in command or 'laugh' in command:
            joke_text = pyjokes.get_joke()
            print(joke_text)
            talk(joke_text)
            responses.append(f"{joke_text}\n")
            sys.stdout.flush()       
        elif any(keyword in command for keyword in ['who is','find', 'tell me about', 'what', 'meaning', 'how', 'whom', 'when', 'where','why']):
            # Extracting the relevant part for the search
            search_query = re.sub(r'google|search', '', command, flags=re.IGNORECASE).strip()
            responses.append(f"Searching Google for: {search_query}\n")
            # Performing the Google search
            talk(f"Searching Google for: {search_query}")
            talk("pleasse check out this website")
            try:
                results = search(search_query)
                for result in results:
                    print(result)
                    # talk(result)
                    responses.append(f"{result}\n")
                    my_custom_time.sleep(2)  # Introduce a delay of 2 seconds between requests
                    break  # Break after the first result
            except StopIteration:
                print("No results found.") 
                responses.append("Sorry, can you please repeat that\n")
        else:
            # print("Sorry :( I could not get it...Please repeat")
            talk("sorry; can you please repeat that")
            responses.append("Sorry, can you please repeat that\n")

        return responses

talk("hi what's up;what can i do for you")
runAlexa()       



# my original code ends here









