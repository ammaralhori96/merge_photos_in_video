import os
import cv2
import numpy as np
from moviepy.editor import VideoFileClip,AudioFileClip, concatenate_videoclips
import arabic_reshaper
from PIL import ImageFont, ImageDraw, Image
from bidi.algorithm import get_display
import soundfile as sf
import time
fbsNumper=100
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip

backSoundName=["The-Four-Seasons",]
backSoundNam=backSoundName[0]
fontSize=30
soundUser=str(input("video sound  y or n: "))  


with open('textSp.txt', 'r', encoding="utf-8") as filee:
            texti = filee.readlines()
def reanameFilesImage():
    path = 'videos'
    # الحصول على قائمة بأسماء جميع الملفات داخل المجلد
    files = os.listdir(path)


    # حلقة تكرارية لإعادة تسمية الملفات
    for file_name in files:
        # الحصول على المسار الكامل للملف
        file_path = os.path.join(path, file_name)
        
        # إعادة تسمية الملف باستخدام رقم فريد
        new_file_name = "video.mp4"
        new_file_path = os.path.join(path, new_file_name)
        os.rename(file_path, new_file_path)
reanameFilesImage()
exec(open('addingIcon.py', encoding='utf-8').read())
# Load video
video_path = 'output\\video.mp4'
audio = AudioFileClip(video_path)
video = VideoFileClip(video_path)

def put_arabic_text(img, text, text_offset, textColor):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text) 
    fontpath = "assets\\arial.ttf" # <== https://www.freefontspro.com/14454/arial.ttf  
    font = ImageFont.truetype(fontpath, fontSize)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text(text_offset,bidi_text, font = font, fill=textColor,)
    return np.array(img_pil)


cap = cv2.VideoCapture(video_path)


# Get video dimensions
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))



#print(height)
fps = int(cap.get(cv2.CAP_PROP_FPS))

#Define text to display

font_scale = 1
thickness = 2
font = cv2.FONT_HERSHEY_SIMPLEX
text_color = (0, 0, 255)

# Create a VideoWriter object to save the output video
out = cv2.VideoWriter("assets\\output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))


# Loop through each frame of the video
x=0
n=0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if x<fbsNumper :
        text =texti[n]
    x+=1
    if x==fbsNumper and n != len(texti)-1:
        x=0
        n+=1
    # Create a black rectangle to display the text on
    text_bg = np.zeros((height, width, 3), dtype=np.uint8)
    #print(text)
    # Get the size of the text to be displayed
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)

    # Calculate the position of the text
    #text_x = int((width - text_width) / 2)
    # text_y = int((height - text_height) / 2)

    # Draw the text on the black rectangle
    # cv2.putText(text_bg, text, (text_x, text_y), font, font_scale, text_color, thickness)

    # Create a mask for the text
    text_mask = cv2.cvtColor(text_bg, cv2.COLOR_BGR2GRAY)
    ret, text_mask = cv2.threshold(text_mask, 10, 255, cv2.THRESH_BINARY)

    # Invert the mask so the text is white
    text_mask_inv = cv2.bitwise_not(text_mask)

    # Create a masked frame by blending the original frame with the text background
    masked_frame = cv2.bitwise_and(frame, frame, mask=text_mask_inv)
    masked_text_bg = cv2.bitwise_and(text_bg, text_bg, mask=text_mask)
    masked_frame = cv2.add(masked_frame, masked_text_bg)
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    #text_x = int((width - text_size[1]) / 2)
    text_x = int((width / 2 )- (text_width / 2))#int((img.shape[1] - (text_width / 2)) / 2)
    text_y = masked_frame.shape[0] - text_size[1] - 10
    font_color = (0, 0, 0)
    bg_color = (255, 255, 255)  # Green background color
    w = text_width -70
    h = text_size[1] + 30
    cv2.rectangle(masked_frame, (10,text_y-20), (text_x+w , text_y + h+30), bg_color, -1)
            
    img = put_arabic_text(masked_frame, text, (10, height-50), font_color)
    # Write the frame to the output video
    out.write(img)

    # # Show the video with the text for 5 seconds, then continue without text
    # for i in range(3 * fps):
    #     ret, frame = cap.read()
    #     if not ret:
    #         break
    #out.write(frame)

cap.release()
out.release()




# قراءة الفيديو والحفاظ على مقاساته
video = VideoFileClip("assets\\output.mp4")
if soundUser == "y":
    # قراءة الملف الصوتي الأصلي
    audio = AudioFileClip('videos\\video.mp4')
    
    
else:
    sound1 = AudioFileClip(video_path)
    number_string = sound1.duration/60
    print("sound1.duration")
    print(sound1.duration)
    print("number_string")
    print(number_string)
    number_string = str(round(number_string, 2))
    parts = number_string.split(".")
    minutes = int(parts[0])   # يحتوي على الأرقام قبل الفاصلة العشرية (3)
    seconds = float( sound1.duration-minutes*60)   # يحتوي على الأرقام بعد الفاصلة العشرية (0.14159)

    #seconds=math.ceil(seconds)
    import subprocess

    # الملف الصوتي المراد قصه
    audio_file = "assets\\"+backSoundNam+".mp3"

    # معلومات الجزء المراد قصه
    start_time = "00:00:00"
    end_time = "00:"+str(minutes)+":"+str(seconds)

    # اسم الملف الجديد الذي سيتم حفظه بعد القص
    output_file = "assets\\finalSound.mp3"

    # الأمر الذي يتم تنفيذه لقص الملف الصوتي
    subprocess.call(['ffmpeg', '-i', audio_file, '-ss', start_time, '-to', end_time, '-c', 'copy', output_file])

    sound2, samplerateu = sf.read(output_file)

    sound2 = sound2 * 0.1 # increase volume by 2x
    # save the combined sound to a file
    sf.write(output_file, sound2, samplerateu)
    audio = AudioFileClip("assets\\finalSound.mp3")
    # دمج الفيديو والصوت
final_clip = CompositeVideoClip([video.set_audio(audio)])

# حفظ الفيديو مع الصوت الأصلي وحفاظ على مقاساته
final_clip.write_videofile("output\\video.mp4", codec='libx264', audio_codec='aac', fps=video.fps)




