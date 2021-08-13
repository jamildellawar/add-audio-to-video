import cv2
import moviepy.editor as mpe
import numpy as np

# Example Files
picturePath = 'carnage.png'
audio = "clarao final.mp3"
pathOut = 'videoOut1.mp4'
seconds = 60


# Frames Per Second (fps) 
fps = 15


img = cv2.imread(picturePath)


height, width, layers = img.shape
size = (width,height)
    
# Creating the VideoWriter and insterting the image for however many seconds
# at this certain FPS
out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
for i in range(15*seconds):
    # writing to a image array
    out.write(img)
out.release()

# Create a VideoFileClip to add the audio to
silent_clip = mpe.VideoFileClip(pathOut)

# Add the audio and export it
clip_with_audio = silent_clip.set_audio(mpe.AudioFileClip(audio).set_end(seconds))
clip_with_audio.write_videofile("final.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
