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

# Example script — calculates the cost of coffee orders

# Set prices for different drinks
espresso_price = 3.50
latte_price = 4.50
cappuccino_price = 4.00

# Get the number of drinks ordered
num_espresso = 2
num_latte = 3
num_cappuccino = 1

# Calculate the total cost
total = (num_espresso * espresso_price) + \
        (num_latte * latte_price) + \
        (num_cappuccino * cappuccino_price)

# Check if total is above the minimum for a discount
discount = 0.10
if total > 20:
    total = total - (total * discount)  # Apply 10% discount
    print("Discount applied!")
else:
    print("No discount available")

# Print the final total
print(f"Total cost: ₦{total}")
print("Thank you for your order!")

def make_custom_drink(base_drink, milk_type, sugar_packets):
    # Assemble the descriptive string step-by-step
    description = f"{base_drink} with {milk_type} milk"
    
    if sugar_packets > 0:
        description = description + f" and {sugar_packets} sugar packets"
        
    return description

# Generate distinct order strings
order1 = make_custom_drink("Latte", "almond", 2)
order2 = make_custom_drink("Cappuccino", "whole", 0)

print(order1) # "Latte with almond milk and 2 sugar packets"
print(order2) # "Cappuccino with whole milk"

safety-monitored conditional loop:

# Check soil condition dynamically
while soil_moisture_percentage < 45.0:
    water_valve_active = True
    dispense_water(seconds=10)
    soil_moisture_percentage = read_moisture_sensor() # Update state variable
    
water_valve_active = False # Safe shutdown


