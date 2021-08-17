# check out the video I made on the topic of text to speech with google in python
# https://youtu.be/yPhH0Fw_GFM

# if you have watched this video, you should not have any problem in the difficult part...that is the speaking part..
# the remaining file is just simple file handling in python
# make the necessary changes according to your need

#pip install gtts --> gtts is the google text to speech package
#pip install pyglet --> pyglet is the media manager for python
from gtts import gTTS
import pyglet
import os
from time import sleep

def say(sentence):
    #this function uses gtts to speak whatever is in the argument
    output=gTTS(text=sentence,lang='en',slow=False) # get the audio from google
    filename="temp.mp3"  # filename of the file where we will save the audio that we got from google
    output.save(filename) # saving the audio
    voice=pyglet.media.load(filename,streaming=True) # now we open that audio file with pyglet
    voice.play() # we play the audio file
    sleep(voice.duration)   # wait till the audio is played completely
    os.remove(filename) # delete the temporary audio file, otherwise it will take up a lot of memory
# main program starts from here:

path_file=r"E:\book.txt" # replace this with the path of your text file
file=open(path_file,'r') # open the file
while(True): # start an infinite loop
    line=file.readline() # read lines one by one
    if(line==""): # if the line that was read is empty, that means the text file has no more text
        break # break the infinite loop
    say(line) # say the line loudly  with gTTS
file.close() # close the file after the work is complete