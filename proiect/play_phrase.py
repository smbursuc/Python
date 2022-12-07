import tkinter as tk
import os
import random
from gtts import gTTS
from gtts import lang
from playsound import playsound


last_file = ''

def find_language_code(language):
    for key,value in lang.tts_langs().items():
        if value == language:
            return key

def check_if_file_exists(file):
    if os.path.isfile(file):
        return True
    else:
        return False

def play_phrase():
    global last_file
    language = current_language.get()
    language_code = find_language_code(language)
    if len(entry.get())>100:
        print("Phrase is too long. There can only be 100 characters or less in each line. Entry line length has been reduced to 100.")
    tts = gTTS(text=entry.get()[:100], lang=language_code)
    # name = entry.get().replace(" ", "_")
    # name = re.sub('\W+','', name)
    random_nr = random.randint(0,100000)
    if check_if_file_exists(str(random_nr) + ".mp3"):
        os.remove(str(random_nr) + ".mp3")
    filename = str(random_nr) + ".mp3"
    tts.save(filename)
    playsound(".\\" + filename, block=False)
    if last_file != '':
        if os.path.isfile(last_file):
            os.remove(last_file)
        last_file = filename
    else:
        last_file = filename


root = tk.Tk()
root.title("Text to speech program")
root.geometry("800x600")
greeting = tk.Label(text="Text to Speech")
greeting.pack()
entry = tk.Entry()
entry.pack()
button = tk.Button(root, text ="Play", command = play_phrase)
button.pack()


current_language = tk.StringVar(root)
current_language.set("English") # default value
langs = list(lang.tts_langs().values())
w = tk.OptionMenu(root, current_language, *langs)
w.pack()

message = tk.Label(text="Audio file is saved in the same directory as the script but will be deleted if you play another phrase")
message.pack()

def on_closing():
    if last_file!='':
        if os.path.isfile(last_file):
            os.remove(last_file)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()



