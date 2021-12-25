# ---------- Packages -----------


import os
from os.path import isfile, join
from playsound import playsound
import tkinter as tk
import fnmatch
from pygame import mixer


# ------------ Canvas -------------


canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x600")
canvas.config(bg = 'black')


# ------------ Assets -------------

# Set file directory and the type of file as .mp3
rootpath = os.getcwd() + r"\songs"
pattern = "*.mp3"

mixer.init()

# Create the buttons
prev_img = tk.PhotoImage(file = os.getcwd() + r"\assets\prev_img.png")
pause_img = tk.PhotoImage(file = os.getcwd() + r"\assets\pause_img.png")
next_img = tk.PhotoImage(file = os.getcwd() + r"\assets\next_img.png")
play_img = tk.PhotoImage(file = os.getcwd() + r"\assets\play_img.png")
stop_img = tk.PhotoImage(file = os.getcwd() + r"\assets\stop_img.png")


# ------------ Methods -------------

# Select Button
def select_song():
    # Get Selection -> Play
    label.config(text = listbox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    mixer.music.play()

# Stop Button
def stop_song():
    # Stop
    mixer.music.stop()
    listbox.select_clear('active')

# Next Button
def next_song():
    # Check current song -> Send next song value-> Play -> Update selection
    next_song = listbox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listbox.get(next_song)
    label.config(text = next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listbox.select_clear(0, 'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

# Previous Button
def prev_song():
    # Check current song -> Send prev song value-> Play -> Update selection
    prev_song = listbox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listbox.get(prev_song)
    label.config(text = prev_song_name)
    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()

    listbox.select_clear(0, 'end')
    listbox.activate(prev_song)
    listbox.select_set(prev_song)

# Pause Button
def pause_song():
    #  Pause  makes Play and vice versa
    if pausebutton["text"] == "Pause":
        mixer.music.pause()
        pausebutton["text"] = "Play"
    else:
        mixer.music.unpause()
        pausebutton["text"] = "Pause"


# ------------ Listboxes -------------

# Song list
listbox = tk.Listbox(canvas, fg = "cyan", bg = "black", width = 100 , font = ('poppins',12))
listbox.pack(padx = 20, pady = 20)

# Current song
label = tk.Label(canvas,text = '', bg = 'black', fg ='white', font = ('poppins',15))
label.pack(pady = 20)

# Frame
top = tk.Frame(canvas, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center')

# Buttons
prevbutton = tk.Button(canvas, text = "Prev", image = prev_img, bg = 'black', borderwidth = 0 , command = prev_song)
prevbutton.pack(pady=20, in_ = top , side = 'left')

stopbutton = tk.Button(canvas, text = "Stop", image = stop_img, bg = 'black', borderwidth = 0 , command = stop_song )
stopbutton.pack(pady=20, in_ = top , side = 'left')

playbutton = tk.Button(canvas, text = "Play", image = play_img, bg = 'black', borderwidth = 0 , command = select_song)
playbutton.pack(pady=20, in_ = top , side = 'left')

pausebutton = tk.Button(canvas, text = "Pause", image = pause_img, bg = 'black', borderwidth = 0 , command = pause_song)
pausebutton.pack(pady=20, in_ = top , side = 'left')

nextbutton = tk.Button(canvas, text = "Next", image = next_img, bg = 'black', borderwidth = 0 , command = next_song)
nextbutton.pack(pady=20, in_ = top , side = 'left')


# ------------ Main Execution -------------


#Getting the mp3 files in directory and sending to listbox
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listbox.insert('end', filename)


canvas.mainloop()