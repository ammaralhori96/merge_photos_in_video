
import cv2
import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import arabic_reshaper
from bidi.algorithm import get_display
import numpy as np
from PIL import ImageFont, ImageDraw, Image
from gtts import gTTS
import soundfile as sf
import numpy as np

def put_arabic_text(img, text, text_offset):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text) 
    fontpath = "assets\\arial.ttf" # <== https://www.freefontspro.com/14454/arial.ttf  
    font = ImageFont.truetype(fontpath, 32)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text(text_offset,bidi_text, font = font)
    return np.array(img_pil)

def merging_sounds():



    # load the audio files
    sound1, samplerate = sf.read("assets\\hello.mp3")
    sound2, _ = sf.read("assets\\The-Four-Seasons.mp3")


    # adjust the volume of each sound
    sound1 = sound1 * 2  # decrease volume by half
    sound2 = sound2 * 0.5 # increase volume by 2x

    # make sure both sounds have the same length
    min_len = min(len(sound1), len(sound2))
    sound1 = np.tile(sound1[:min_len], (sound2.shape[1], 1)).T
    sound2 = sound2[:min_len]

    # mix the sounds together
    combined = np.add(sound1, sound2)



    # save the combined sound to a file
    sf.write("assets\\mergingSound.mp3", combined, samplerate)

    # تحميل مقطعي الصوت
    sound1, sample_rate = sf.read('assets\\mergingSound.mp3', )
    sound2, sample_rate = sf.read("assets\\The-Four-Seasons.mp3")
    # adjust the volume of each sound
    # دمج مقطعي الصوت
    combined_sound = np.append(sound1, sound2, axis=0)

    # حفظ الملف المدمج
    sf.write('assets\\mergingSoundd.mp3', combined_sound, samplerate)


newText=[]
with open('assets\\textSp.txt', 'r', encoding="utf-8") as file:
    nymperfound=25
    z=0
    n=0
    u=file.read()
    u = u.replace("\n", " " )
    print(u)

    line = u.strip()
      
    #print("ssss")
    for i in range(0, len(line)):
        marks=[",","،",".","?",":","!",";","؛",] 
        if (i >=z+nymperfound and line[i] ==" ") or (i >=z and line[i] in marks) :
            n=i

        if n>z:
            #print(n)
            newText.append(line[z:n])
            #print(line[z:n])
            z=n
            if (z +nymperfound>=len(line)) and (line[z+2:len(line)-2] not in line[len(line)-30:len(line)]  ):
                # print(line[z+4:len(line)-4] not in newText[len(newText)-1])
                # print(newText[len(newText)-1])
                # print(line[z+4:len(line)-4])
                newText.append(line[z:len(line)])
    
    if len(newText)!=0:
        with open('assets\\textSp.txt', 'w', encoding="utf-8") as filee:
            #print("hhhhhh")
            # كتابة السطور المقطوعة في الملف الجديد
            for line in newText:
                filee.write(line + '\n')
    else :
        newText=u
    
            

with open('assets\\textSp.txt', 'r', encoding="utf-8") as file:
    text = file.read()



# تحويل النص إلى ملف صوتي
tts = gTTS(text=text, lang='es', slow=True)
tts.save("assets\\hello.mp3")
# set up video parameters
fps = 0.4
width = 480
height = 480

merging_sounds()
# specify the path to your images
img_dir = 'images'

# get a list of all the image file names
img_files = sorted([f for f in os.listdir(img_dir) if f.endswith('.jpg')])
 

while len(img_files) < len(newText):
    x=len(newText)-len(img_files)
    img_files= img_files+ img_files[0:x]
    print(x)
print("newText " +str(len(newText)))
print("img_files "+str(len(img_files)))
print("img_files")
print(img_files)


# create a video writer object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output\\output.mp4', fourcc, fps, (width, height))

# loop over each image and add it to the video
x=0
for img_file in img_files:
    # read the image file
    img = cv2.imread(os.path.join(img_dir, img_file))
    # resize the image to fit the video frame
    img = cv2.resize(img, (width, height))

    # add text to the image
    #text = img_file
    #text="سيشلبيبياش  لبيبياش نمنمنمن"
    #text="mucó mucó  é ç  ê â  î ô û"
    if x < len(newText):
        text= newText[x]
    else:
        text= newText[len(newText)-1]
    #text= "é, è, ê, ë, à, â, ô, î, ï, û, ç, œ. ñ, ü, á, é, í, ó, ú, ¿, ¡."
    text_width = len(text) * 13
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255)
    thickness = 2
   
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    #text_x = int((width - text_size[1]) / 2)
    text_x = int((width / 2 )- (text_width / 2))#int((img.shape[1] - (text_width / 2)) / 2)
    text_y = img.shape[0] - text_size[1] - 10
    bg_color = (0, 0, 0)  # Green background color
    w = text_width+ 30
    h = text_size[1] + 30
    # Draw the background rectangle
    cv2.rectangle(img, (text_x,text_y-25), (text_x+w , text_y-10 + h), bg_color, -1)
    
    # text_x = int((img.shape[1]) / 2) + int(text_size[0] / 2)
    # text_x = int((img.shape[1] + (text_width / 2)) / 2)
    #cv2.putText(img, text , (text_x, text_y), font, font_scale, font_color, thickness, cv2.LINE_AA)
    # img = put_arabic_text(img, text, (200, 450))
    img = put_arabic_text(img, text, (text_x, 430))

    # write the image to the video
    out.write(img)
    x+=1

    

# release the video writer object
out.release()


# Load the video and audio clips
video = VideoFileClip('output\\output.mp4')
audio = AudioFileClip('assets\\mergingSoundd.mp3')

# Set the audio clip to the same duration as the video clip
audio = audio.set_duration(video.duration)

# Concatenate the video clip and audio clip
final_clip = video.set_audio(audio)

# Write the final clip to a new file
final_clip.write_videofile("output\\video_with_sound.mp4")