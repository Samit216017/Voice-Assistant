import os
import subprocess as sp
import socket

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
    
def open_notepad():
    codePath = 'C:\\Windows\\notepad.exe'
    os.startfile(codePath)
    #sp.Popen(codePath)
    
def Play_Music():
    music_dir = 'D:\\Semester4\\4Th sam project_New\\Songs'
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))
    
def open_calculator():
    codePath = 'C:\\Windows\\System32\\calc.exe'
    sp.Popen(codePath)
    
def open_cmd():
    os.system('start cmd')
    
def open_vs_code():
    codePath = 'C:\\Users\\Samit Mazumder\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
    sp.Popen(codePath)
    
def open_powerpoint():
    codePath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
    sp.Popen(codePath)
    
def open_excel():
    codePath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
    sp.Popen(codePath)
    
def open_word():
    codePath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
    sp.Popen(codePath)
    
def open_sublime():
    codePathe = 'C:\\Program Files\\Sublime Text 3\\sublime_text.exe'
    sp.Popen(codePathe)
    
def open_paint():
    codePath = 'C:\\Users\\Samit Mazumder\\AppData\\Local\\Microsoft\\WindowsApps\\Microsoft.Paint_8wekyb3d8bbwe\\mspaint.exe'
    sp.Popen(codePath)
    
def play_Alarm_Sound():
    alarm = 'D:\\Semester4\\4Th sam project_New\\Songs'
    songs = os.listdir(alarm)
    print(songs)
    os.startfile(os.path.join(alarm, songs[0]))
    
# def open_discord():
    
    
# def find_my_ip():
#     hostname = socket.gethostname()
#     ip_address = socket.gethostbyname(hostname)
#     return ip_address["ip"]