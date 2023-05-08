from gtts import gTTS
import speech_recognition as sr
import random
import os
#from goto import goto, label
import speech_recognition as sr
import subprocess
import datetime

def speak_to_speaker(text):
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save("tts.mp3")
    os.system("mpg321 -q tts.mp3")
speak_to_speaker('Say A Command')

def beep_high():
    os.system("mpg321 -q beep_hi.mp3")


def beep_low():
    os.system("mpg321 -q beep_lo.mp3")

def recognize_speech_from_mic(recognizer, microphone, timeout=1):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=timeout)
    try:
        response = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        response = None
    except sr.RequestError:
        response = None
    return response

def promptfile():
    speak_to_speaker("Speak File Name")
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    response = recognize_speech_from_mic(recognizer, microphone, timeout=3)
    if response is not None:
        print(f"You said: {response}")
        fname=response
    else:
        print("Sorry, I didn't catch that.")
    return fname



# Usage example:
while True:
    print("Say Something:: ")
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    speak_to_speaker('say a command')
    response = recognize_speech_from_mic(recognizer, microphone, timeout=3)
    if response is not None:
        print(f"You said: {response}")
    else:
        print("Sorry, I didn't catch that.")

    # Get user input
    if "list files" in response:
        beep_low()
        command = "ls"
    elif "hello" in response:
        beep_low()
        speak_to_speaker("hi,how may i help you")
    elif "list file permissions" in response:
        beep_low()
        command = "ls -l"
    elif "shutdown" in response:
        beep_low()
        command = "shutdown -h now"
    elif "current working directory" in response:
        beep_low()
        command = "pwd"
    elif "list hidden files" in response:
        beep_low()
        command = "ls -a"
    elif "show date" in response:
        beep_low()
        command = "date"
    elif "show day" in response:
        current_date = datetime.date.today()
        weekday_name = current_date.strftime("%A")
        print(weekday_name)
    elif "show time" in response:
        beep_low()
        current_time = datetime.datetime.now().time()
        print(current_time)
    elif "show calendar" in response:
        beep_low()
        command = "cal"
    elif "go to home directory" in response:
        beep_low()
        command = "cd ~"
    elif "go to root directory" in response:
        beep_low()
        command = "cd /."
    elif "go to user directory" in response:
        beep_low()
        command = "cd /home"
    elif "take snapshot" in response:
        beep_low()
        command = "scrot screenshot.png"
    elif "show network status" in response:
        beep_low()
        command = "ifconfig"
    elif "create a file" in response:
        beep_low()
        fname = promptfile()
        command = "touch " + fname
    elif "delete a file" in response:
        beep_low()
        fname = promptfile()
        command = "rm " + fname
    elif "open nano editor" in response:
        beep_low()
        fname = promptfile()
        command = "nano " + fname
    elif "open editor" in response:
        beep_low()
        fname = promptfile()
        command = "gedit " + fname

    elif "show username" in response:
        beep_low()
        command = "whoami"
    elif "tell the file type" in response:
        beep_low()
        fname = promptfile()
        command = "file " + fname
    elif "manual of any command" in response:
        beep_low()
        fname = promptfile()
        command = "man " + fname
    elif "make new directory" in response:
        beep_low()
        fname = promptfile()
        command = "mkdir " + fname
    elif "login as root" in response:
        beep_low()
        command = "sudo " + fname
    elif "list users" in response:
        beep_low()
        command = "cat /etc/passwd"

    elif "who created you" in response:
        beep_low()
        speak_to_speaker('seher,aamna,robaas created this')

    else:
        beep_high()
        speak_to_speaker('invalid command')
    # Execute the command
    output = subprocess.check_output(command, shell=True)

    # Print the output
    print(output.decode('utf-8'))
    ch=str(input("Do u wish to continue?"))
    if "yes" in ch:
    		continue
    else:
    	break		
