import cv2
import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import arabic_reshaper
from bidi.algorithm import get_display
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def put_arabic_text(img, text, text_offset):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text) 
    fontpath = "arial.ttf" # <== https://www.freefontspro.com/14454/arial.ttf  
    font = ImageFont.truetype(fontpath, 32)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text(text_offset,bidi_text, font = font)
    return np.array(img_pil)
    

# set up video parameters
fps = 0.4
width = 640
height = 480

# specify the path to your images
img_dir = 'images'

# get a list of all the image file names
img_files = sorted([f for f in os.listdir(img_dir) if f.endswith('.jpg')])

# create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

# loop over each image and add it to the video
for img_file in img_files:
    # read the image file
    img = cv2.imread(os.path.join(img_dir, img_file))
    # resize the image to fit the video frame
    img = cv2.resize(img, (width, height))

    # add text to the image
    text = img_file
    text=" نمنمنمنم شكينكبلنشك"
    text_width = len(text) * 10
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255)
    thickness = 2
   
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]

    text_x = int((width / 2 )- (text_width / 2))#int((img.shape[1] - (text_width / 2)) / 2)
    text_y = img.shape[0] - text_size[1] - 10
    bg_color = (0, 0, 0)  # Green background color
    w = text_width+ 30
    h = text_size[1] + 30
    # Draw the background rectangle
    cv2.rectangle(img, (text_x -10,text_y-25), (text_x-10 + w, text_y-10 + h), bg_color, -1)
    # text_x = int((img.shape[1]) / 2) + int(text_size[0] / 2)
    # text_x = int((img.shape[1] + (text_width / 2)) / 2)
    print(text_x)
    # cv2.putText(img, text , (text_x, text_y), font, font_scale, font_color, thickness, cv2.LINE_AA)
    # img = put_arabic_text(img, text, (200, 450))
    img = put_arabic_text(img, text, (text_x, 430))

    # write the image to the video
    out.write(img)

    

# release the video writer object
out.release()


# Load the video and audio clips
video = VideoFileClip('output.mp4')
audio = AudioFileClip('The-Four-Seasons.mp3')

# Set the audio clip to the same duration as the video clip
audio = audio.set_duration(video.duration)

# Concatenate the video clip and audio clip
final_clip = video.set_audio(audio)

# Write the final clip to a new file
final_clip.write_videofile("video_with_sound.mp4")