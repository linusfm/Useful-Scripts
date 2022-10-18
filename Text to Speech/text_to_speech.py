from gtts import gTTS
import os 

name = input("Folder name: ")

file = open(name + "/" + name + ".txt", "r")
text = file.read().replace("\n", ",")

language = "en"

output = gTTS(text=text, lang=language, slow=False, )

output.save(name + "/" + name +".mp3")

os.system("start " + name + "/" + name + ".mp3")