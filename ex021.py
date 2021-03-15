#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load(r'C:\Users\kostf\Documents\Python\Exercicíos\ex021.mp3')
mixer.music.play()