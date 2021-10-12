import pyttsx3
import os

fileName = input("Enter file name: ")
with open(fileName, "r") as f:
    file = f.readlines()
    print(file)
engine = pyttsx3.init()
engine.say(file)
engine.runAndWait()