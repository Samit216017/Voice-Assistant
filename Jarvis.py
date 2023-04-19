import datetime
import os
import smtplib, ssl
import webbrowser as web
import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit
import time
import subprocess
import random
import requests
import json
import sys
from datetime import date
from flask import Flask
from email.message import EmailMessage
from random import choice
from talk import opening_text
from Functions.offline_ops import*
from Functions.online_ops import*
from pprint import pprint

from PyQt5 import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.uic import*
from jarvisGui import*

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        print("Good Morning")
        speak("Good Morning")
    elif hour>=12 and hour<18:
        print("Good afternoon")
        speak("Good afternoon")
    else:
        print("Good evening")
        speak("Good evening")
    print("Hello Sir, I am Jarvis. Please tell me how may I halp you.")
    speak("Hello Sir, I am Jarvis. Please tell me how may I halp you.")
    
def Play_alarm():
    speak("please enter the time sir")
    alarmTime = input("Time input format is hh:mm:AM/PM\nEnter the time sir: ")
    while True:
        NowTime = datetime.datetime.now().strftime("%I:%M:%p")
        if NowTime == alarmTime:
            print("Its time to wake up sir")
            speak("its time to wake up sir")
            play_Alarm_Sound()
            time.sleep(27)
            speak("its time to wake up sir")
            speak("alarm closed")
            break
        break


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        
    def run(self):
        self.tasks()
        
    def takeCommand(self):
    #it takes microphone input from the users and return string outputs
    
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        
            if 'exit' in query or 'stop' in query:
                hour = int(datetime.datetime.now().hour)
                if hour>=22 or hour<6:
                    speak("Good night sir, take care!")
                else:
                    speak("Have a good day sir.")
                exit(app.exec_())
                #exit()
            
        except Exception as e:
            print(e)
            print("Say that again please...")
            speak("Say that again please...")
            return "None"
        return query
        
    def tasks(self):
        wishMe()
        
        while True:
            query = self.takeCommand().lower()
            
            if 'wish me' in query:
                wishMe()
                
            elif 'thank you' in query:
                speak("Welcome sir.")
                
            elif 'good morning' in query:
                hour = int(datetime.datetime.now().hour)
                if hour>=6 and hour<12:
                    speak("Good morning sir. Are you want to lesten news?")
                    ans = self.takeCommand().lower()
                
                else:
                    speak("It is not Morning sir.")
                
            elif 'good afternoon' in query:
                hour = int(datetime.datetime.now().hour)
                if hour>=12 and hour<18:
                    wishMe()
                else:
                    speak("It is not Afternoon sir.")
                
            elif 'good evening' in query:
                hour = int(datetime.datetime.now().hour)
                if hour>=18 or hour<6:
                    wishMe()
                else:
                    speak("It is not Evening sir.")
                
            elif 'good night' in query:
                hour = int(datetime.datetime.now().hour)
                if hour>=22 or hour <6:
                    speak("Good night sir, have a sweet dreams")
                    exit()
                else:
                    speak("It is not night sir.")
                
            elif 'your name' in query:
                print("My name is Jarvis. How may I help you?")
                speak("My name is Jarvis. How may I help you?")
                
            elif 'how are you' in query:
                print("I am fine sir. What about you? How may I help you?")
                speak("I am fine sir. What about you? How may I help you?")
                
            elif 'hello' in query:
                print("Hello sir. How may I help you?")
                speak("Hello sir. How may I help you?")
                
            elif 'hello jarvis' in query:
                print("Oh, hello, sir.")
                speak("Oh, hello, sir.")
                
            elif 'what are you doing' in query:
                print("Now I am trying to help you. What can I do for you sir?")
                speak("Now I am trying to help you. What can I do for you sir?")
        
            elif 'open camera' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                open_camera()
            
            elif 'open notepad' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                open_notepad()
            
            elif 'wikipedia' in query:
                print("What do you want to search on wikipedia, sir?")
                speak("What do you want to search on wikipedia, sir?")
                search_query = self.takeCommand().lower()
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                results = search_on_wikipedia(search_query)
                speak("According to wikipedia")
                print(results)
                speak(results)
            
            elif 'open youtube' in query:
                print("What do you want to plat on Youtube, sir?")
                speak("What do you want to plat on Youtube, sir?")
                video = self.takeCommand().lower()
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                play_on_youtube(video)
            
            elif 'open google' in query:
                print("What do you want to search on google, sir")
                speak("What do you want to search on google, sir")
                query = self.takeCommand().lower()
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                search_on_google(query)
                
            elif 'open firefox' in query:
                print("What do you want to search on firefox, sir")
                speak("What do you want to search on firefox, sir")
                query = self.takeCommand().lower()
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                search_on_firefox(query)
            
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                
            elif 'date' in query:
                today = date.today()
                strDate = today.strftime("%d %B, %y")
                speak(f"sir, the date is {strDate}")
            
            elif 'play music' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                Play_Music()

            elif 'open calculator' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                open_calculator()
            
            elif 'joke' in query:
                print("Hope you like this one sir")
                speak("Hope you like this one sir")
                joke = get_random_joke()
                print(joke)
                speak(joke)
            
            elif 'open command prompt' in query or 'open cmd' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                open_cmd()
            
            elif 'ip address' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                ip_address = find_my_ip()
                print(f'Your IP Address is {ip_address}')
                speak(f'Your IP Address is {ip_address}')
            
            elif 'whatsapp' in query:
                speak("Sir, please tell me the number.")
                number = input("Enter the number")
                print("What is the messsege sir?")
                speak("What is the messsege sir?")
                message = self.takeCommand()
                speak("Enter hour and minute sir")
                hour = int(input("Enter hour: "))
                minute = int(input("Enter minute sir: "))
                speak("Just a second, sir")
                send_messege(number, message, hour, minute)
                speak("I have sent the messege sir.")
                
            elif 'open gmail' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                open_gmail()
                
            elif 'send email' in query:
                speak("Enter your email address sir")
                sender_address = input("Enter your email address: ")
                speak("Please enter your email login password sir")
                password = input("Enter your email login password: ")
                speak("Enter the receiver address sir")
                receiver_address = input("Enter receiver email address: ")
                print("What should be the subject sir?")
                speak("What should be the subject sir?")
                subject = self.takeCommand().capitalize()
                print("What is the message sir?")
                speak("What is the message sir?")
                message = self.takeCommand().capitalize()
                if send_email(sender_address,password,receiver_address,subject,message):
                    print("I have sent the email sir.")
                    speak("I have sent the email sir")
                else:
                    print("Something went wrong while I was sending the mail. Please check the error logs sir.")
                    speak("Something went wrong while I was sending the mail. Please check the error logs sir.")
                    
            elif 'vs code' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                open_vs_code()
                
            elif 'powerpoint' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                open_powerpoint()
                
            elif 'excel' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                open_excel()
                
            elif 'ms word' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                open_word()
                
            elif 'sublime' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                open_sublime()
                
            elif 'paint' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                open_paint()
                
            elif 'temperature' in query or 'weather' in query:
                print("Please tell me the city name, sir: ")
                speak("Pkease tell me the city name, sir: ")

                city = self.takeCommand().lower()
                print(f"Getting weather report for the city {city}")
                speak(f"Getting weather report for the city {city}")
                temperature, feels_like, humidity, weather_description = get_weather(city)
                print(f"\nTemperature in {city} is: {temperature} degree Celsius, but it feels like {feels_like} degree Celsius")
                print(f"\nHumidity in {city} is: {humidity} %")
                print(f"\nAnd the weather description is {weather_description}")
                speak(f"Temperature in {city} is {temperature} degree celsius, but it feels like {feels_like} degree celsius")
                speak(f"Humidity in {city} is {humidity} percent")
                speak(f"and the weather description is {weather_description}")
                
            elif 'alarm' in query:
                Play_alarm()
                
            # elif 'online music' in query:
            #     wait = choice(opening_text)
            #     print(wait)
            #     speak(wait)
            #     open_online_music()
            
            # elif 'discord' in query:
            #     wait = choice(opening_text)
            #     print(wait)
            #     speak(wait)
            #     open_discord()
            
            elif 'advice' in query:
                wait = choice(opening_text)
                print(wait)
                speak(wait)
                print("\nHere is an advice for you, sir")
                speak("Here is an advice for you, sir")
                advice = get_random_advice()
                print(advice)
                speak(advice)
                
            elif 'trending movies' in query:
                print("Some of the trending movies are: ")
                speak("some of the trending movies are")
                print(*get_trending_movies(), sep="\n")
                speak(f"{get_trending_movies()}")
                
            
            # else:                # For searching anything on google...
            #     pywhatkit.search(query)
            #     speak("these are results on web")
                
            time.sleep(3)





# For start Main
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisGui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
    def startTask(self):
        #self.ui.movie = QtGui.QMovie("D:\jarvis\jarvis1.gif")
        self.ui.movie = QtGui.QMovie("jarvis_1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        # self.ui.movie = QtGui.QMovie("D:\jarvis\jarvis2.gif")
        self.ui.movie = QtGui.QMovie("jarvis_2.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        # self.ui.movie = QtGui.QMovie("D:\jarvis\jarvis3.gif")
        self.ui.movie = QtGui.QMovie("jarvis_3.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss AP")
        label_date = current_date.toString("dd/MM/yyyy")
        self.ui.label_5.setText(label_date)
        self.ui.label_7.setText(label_time)
        

# The main program will be start here
if __name__ == "__main__":
    app = QApplication(sys.argv)
    jarvis = Main()
    jarvis.show()
    exit(app.exec_())