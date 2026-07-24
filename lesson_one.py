import os
import pytube
from moviepy.editor import *

infinity= 2e400
print(infinity)

#string to integer
age = "40"
print(int(age))

#concatenation
first_name = "Damilo"
last_name = "Gwarinpa"
full_name = first_name + " " + last_name
print(full_name)


# Define the YouTube video URL
youtube_url = "https://www.youtube.com/watch?v=E6eKvji_BoE"

# Create a PyTube object and get the audio stream
yt = pytube.YouTube(youtube_url)
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio stream as a temporary file
temp_file = audio_stream.download()

# Convert the audio stream to an MP3 file using MoviePy
audio_clip = AudioFileClip(temp_file)
mp3_file = os.path.join("Give Your own path", "Name.mp3")
audio_clip.write_audiofile(mp3_file)

os.remove(temp_file)

print("Audio extracted and saved as MP3 file to", mp3_file)

def substring_return(text, substring):
    if substring in text:
        return substring
    return none

def substring_search(text, target):
    return target.lower() in text.lower()

def search_name(str, target):
    matches = []
    for t in str:
        if t == target:
            matches.append(t)
    return matches 

class Person:
   def __init__(self, name, age):
        self.name =name
        self.age = age
        print(f"{name} is my name, and I am {age} years old")

joe = Person ("Joe",46)
sam = Person ("Samantha",10)

sub =substring_search("hello my lovely lady", "lady")
call = search_name("my name is joey", "n")
print(call)
print(sub)

re = substring_return("hello duniya", "duniya")
print(re)

