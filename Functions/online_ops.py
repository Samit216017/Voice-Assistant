import pywhatkit as kit
import wikipedia
import requests
import webbrowser
import pyjokes
import smtplib
import ssl
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.request import urlopen
from email.message import EmailMessage
#from decouple import config


#def search_on_web():

# EMAIL = config("EMAIL")
# PASSWORD = config("PASSWORD")
    
    
def search_on_wikipedia(query):
    result = wikipedia.summary(query, sentences=2)
    return result

def play_on_youtube(video):
    #kit.playonyt(video)
    webbrowser.open("https://www.youtube.com/results?search_query=" + video)
    
def search_on_google(query):
    kit.search(query)
    
def search_on_firefox(query):
    firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    firefox.open(query)
    
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def send_messege(number, message, hour, minute):
    kit.sendwhatmsg(f"+91{number}",message,hour,minute)
    
def open_gmail():
    webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
    
def send_email(sender_address, password, receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email['Sunject'] = subject
        email['From'] = sender_address
        email.set_content(message)
        ob = smtplib.SMTP("smtp.gmail.com", 587)
        ob.ehlo()
        ob.starttls()
        ob.login(sender_address,password)
        #ob.send_message(email)
        ob.sendmail(sender_address, receiver_address, email)
        ob.close()
        return True
    except Exception as e:
        print(e)
        return False
    
def get_weather(city):
    api_key = "d953713c6fc225faf3703382e1c0e866"
    # address = "https://api.openweathermap.org/data/2.5/weather?q="
    # full_address = address + city + "&appid=" + api_key + "&units=mertic"
    # response = requests.get(full_address).json()
    
    # if response["cod"] != "404":
    #     x = response["main"]
    #     current_temp = int(x["temp"] - 273.15)
    #     current_humidity = x["humidity"]
    #     y = response["weather"]
    #     weather_description = y[0]["description"]
    #     print("\nTemperature in " + city + " is: " + str(round(current_temp, 0)) + " Celsius\n"
    #           + "Humidity in " + city + " is: " + str(current_humidity) + "%\n"
    #           + "Description: " + str(weather_description))
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=mertic").json()
    
    temperature = response["main"]["temp"]
    feels_like = response["main"]["feels_like"]
    humidity = response["main"]["humidity"]
    weather_description = response["weather"][0]["description"]
    return temperature, feels_like, humidity, weather_description

# def open_online_music():
#     webbrowser.open("")

def get_random_advice():
    advice = requests.get("https://api.adviceslip.com/advice").json()
    return advice["slip"]["advice"]

def get_trending_movies():
    trending_movies = []
    result = requests.get()
        
    
    
# def send_email(receiver_address,subject,message):
#     try:
#         email = EmailMessage()
#         email['To'] = receiver_address
#         email["Subject"] = subject
#         email['From'] = EMAIL
#         email.set_content(message)
#         s = smtplib.SMTP("smtp.gmail.com", 587)
#         s.starttls()
#         s.login(EMAIL, PASSWORD)
#         s.send_message(email)
#         s.close()
#         return True
#     except Exception as e:
#         print(e)
#         return False