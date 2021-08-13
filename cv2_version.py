import cv2
import moviepy.editor as mpe
import numpy as np
import tkinter


# Example Files
print("Make sure to put in all the files necessary in the folder that the file \'cv2_version.py\' is in.")
picturePath = input("What is the name of the picture file (.png or .jpg)? ")
audio = input("What is the name of the audio file (.mp3 or .wav)? ")
pathOut = input("What would you like the final product video to be called? (exclude the \'.mp4\' at the end) ") + ".mp4"
seconds = int(input("How long (in seconds) would you like the video to be? "))

temp_blank_video = "videoWithoutAudio.mp4"

# Frames Per Second (fps) 
fps = 15


img = cv2.imread(picturePath)


height, width, layers = img.shape
size = (width,height)
    
# Creating the VideoWriter and insterting the image for however many seconds
# at this certain FPS
out = cv2.VideoWriter(temp_blank_video,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
for i in range(15*seconds):
    # writing to a image array
    out.write(img)
out.release()

# Create a VideoFileClip to add the audio to
silent_clip = mpe.VideoFileClip(temp_blank_video)

# Add the audio and export it
clip_with_audio = silent_clip.set_audio(mpe.AudioFileClip(audio).set_end(seconds))
clip_with_audio.write_videofile(pathOut, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
