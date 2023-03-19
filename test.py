import cv2
import numpy as np
import moviepy.editor as mp

import os

# Define path to the image folder
image_folder = "images"

# Get list of image files in the folder
image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f)) and f.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

title_text = ["سيسشيب  1", "Hello my friend 2", "Bonjour mon ami", "Hola amigo mío", "Hallo mein Freund 3", "Привет, мой друг 3", "Title 3", "Title 3", "Title 3", "Title 3", "Title 3", "Title 3", "Title 3", "Title 3", "Title 3", "Title 3", "Title 3", "Title 3"]
title_font = cv2.FONT_HERSHEY_SIMPLEX
title_scale = 1.5
title_color = (255, 255, 255) # White
title_bg_color = (0, 0, 255) # Red

# Define video properties
video_width = 640
video_height = 480
fps = 0.4

# Define output video file name and sound file name
output_video_file = "output.mp4"
sound_file = "assets\\The-Four-Seasons.mp3"

# Create an empty video writer object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_video_file, fourcc, fps, (video_width, video_height))

# Loop through image files and add each image to the video with title
for i in range(len(image_files)):
    # Load image and resize to fit video size
    img = cv2.imread(image_files[i])
    img = cv2.resize(img, (video_width, video_height))

    # Add title to the image
    text_size, _ = cv2.getTextSize(title_text[i], title_font, title_scale, thickness=2)
    text_x = int((video_width - text_size[0]) / 2)
    text_y = int(video_height * 0.1)
    cv2.rectangle(img, (text_x - 10, text_y - 10), (text_x + text_size[0] + 10, text_y + text_size[1] + 10), title_bg_color, -1)
    cv2.putText(img, title_text[i], (text_x, text_y + text_size[1]), title_font, title_scale, title_color, thickness=2)

    # Write the image to the video
    out.write(img)

# Release video writer object
out.release()

# Load output video file as a clip
clip = mp.VideoFileClip(output_video_file)

# Load sound file as a clip and set audio duration to match video duration
audio = mp.AudioFileClip(sound_file).set_duration(clip.duration)

# Combine video and sound clips and write to a new file
final_clip = clip.set_audio(audio)
final_clip.write_videofile("final_output.mp4")
