
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
from langdetect import detect
from mutagen.mp3 import MP3

backSoundName=["The-Four-Seasons",]
backSoundNam=backSoundName[0]
#lang=["ar","en","fr","es"]
lang=["ar","en","fr","es"]
titleCaver=[]
titleYoutube=[]
def put_arabic_text(img, text, text_offset, textColor):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text) 
    fontpath = "assets\\arial.ttf" # <== https://www.freefontspro.com/14454/arial.ttf  
    font = ImageFont.truetype(fontpath, 32)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text(text_offset,bidi_text, font = font, fill=textColor,)
    return np.array(img_pil)

def merging_sounds():


    if videoTypeUser != 1:
    # load the audio files
        sound1, samplerate = sf.read("assets\\hello.mp3")
    sound2, samplerateu = sf.read("assets\\"+backSoundNam+".mp3")

    sound2 = sound2 * 0.1 # increase volume by 2x
    if videoTypeUser != 1:
        # adjust the volume of each sound
        sound1 = sound1 * 2  # decrease volume by half
    

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
    if videoTypeUser != 1:
        # حفظ الملف المدمج
        sf.write('assets\\mergingSoundd.mp3', combined_sound, samplerate)
    if videoTypeUser == 1:
        # حفظ الملف المدمج
        sf.write('assets\\mergingSoundd.mp3', sound2, samplerateu)


def smallImageUoutube(caverImage,text1):
 

    # فتح الصورة الأساسية (JPG)
    try:
        base_image = Image.open("images\\"+ caverImage +".jpg")
    except:
        base_image = Image.open("images\\"+ caverImage +".png")

    # فتح الصورة التي سنضيفها فوق الصورة الأساسية (PNG)
    overlay_image = Image.open("assets\\small image youtube caver.png")

    # ضبط حجم الصورة التي سنضيفها فوق الصورة الأساسية
    base_image = base_image.resize(overlay_image.size)

    # وضع الصورة المتحركة فوق الصورة الأساسية
    base_image.paste(overlay_image, (0, 0), overlay_image)
    try:
        # حفظ الصورة الجديدة (يمكن تغيير الاسم والمسار حسب الحاجة)
        base_image.save("assets//caverImage.jpg", "JPEG")
    except:
        rgb_im = base_image.convert('RGB')
        rgb_im.save("assets//caverImage.jpg", "JPEG")




    # فتح الصورة الأساسية (JPG)
    basee_image = Image.open("assets//caverImage.jpg")

    # إنشاء كائن ImageDraw للكتابة على الصورة
    draw = ImageDraw.Draw(basee_image)





    # تحديد نص الكتابة
    language = detect(text1)
    # تحديد لون النص (أسود)
    #color = (255, 242, 0)
    color = (236, 161, 46)

    if language == "ar":
        # تحديد موضع النص على الصورة (يمكن تعديل القيم حسب الحاجة)
        position1 = (50, 589)

        fontSize=110
    else:
         # تحديد موضع النص على الصورة (يمكن تعديل القيم حسب الحاجة)
        position1 = (50, 589)
        fontSize=80


    reshaped_text1 = arabic_reshaper.reshape(text1)

    bidi_text1 = get_display(reshaped_text1) 

    fontpath = "assets\\arial.ttf" # <== https://www.freefontspro.com/14454/arial.ttf  
    font = ImageFont.truetype(fontpath, fontSize)
    draw.text(position1,bidi_text1, font = font,fill=color , stroke_fill= (0, 0, 0), stroke_width=5)

    # حفظ الصورة الجديدة (يمكن تغيير الاسم والمسار حسب الحاجة)
    basee_image.save("caverImage//"+languagee+".jpg", "JPEG")
def titleHundling():
    with open('titleDesc\\caverTitle.txt', 'r', encoding="utf-8") as file:

        lines=file.readlines()
        for line in lines:
                titleCaver.append(line)
              

    with open('titleDesc\\youtubeTitle.txt', 'r', encoding="utf-8") as file:

        lines=file.readlines()
        for line in lines:
            titleYoutube.append(line)
 
videoTypeUser=int(input("enter video voice(0) writing(1) voice+writing(2): "))                
titleHundling()
# for i in range(len(lang)):
#     languagee=lang[i]
#     smallImageUoutube("0", titleCaver[i], )
for i in range(len(lang)):

    languagee=lang[i]
    #smallImageUoutube("Photo0", "المعركة", "الصليبية" , "الاسلامية",)
    smallImageUoutube("0", titleCaver[i], )

    newText=[]
    if videoTypeUser != 0:
        with open('titleDesc\\'+languagee+'.txt', 'r', encoding="utf-8") as file:
            nymperfound=25
            z=0
            n=0
            line=file.read()
            line = line.replace("\n", " " )
            #print(u)

            #line = u.strip()
            
            #print("ssss")
            for i in range(0, len(line)):
                marks=[",","،",".","?",":","!",";","؛",] 
                if (i >=z+nymperfound and line[i] ==" ") or (i >=z and line[i] in marks) :
                    n=i

                if n>z:
                    #print(n)
                    
                    lineE=line[z:n].strip()
                    if lineE != '':
                        newText.append(lineE)
                    #print(line[z:n])
                    z=n
                    if (z +nymperfound>=len(line)) and (line[z+2:len(line)-2] not in line[len(line)-30:len(line)]  ):
                        # print(line[z+4:len(line)-4] not in newText[len(newText)-1])
                        # print(newText[len(newText)-1])
                        # print(line[z+4:len(line)-4])
                        newText.append(line[z:len(line)])
            #ازالة الفراغات
            # for item in newText:
            #     if not item.isalnum():
            #         newText.remove(item)

            if len(newText)!=0:
                with open('titleDesc\\'+languagee+'.txt', 'w', encoding="utf-8") as filee:
                    #print("hhhhhh")
                    # كتابة السطور المقطوعة في الملف الجديد
                    for line in newText:
                        line=line.strip()
                        if line != '':
                            filee.write(line + '\n')
                            
            else :
                newText=line
            
                

    with open('titleDesc\\'+languagee+'.txt', 'r', encoding="utf-8") as file:
        text = file.read()


    if videoTypeUser != 0:
    # تحويل النص إلى ملف صوتي
        if languagee == "ar":
            tts = gTTS(text=text, lang="ar", slow=False)
            fps = 0.33
        elif languagee == "en":
            tts = gTTS(text=text, lang="en", slow=True)
            fps = 0.44
        elif languagee == "fr":
            tts = gTTS(text=text, lang="fr", slow=True)
            fps = 0.4
        elif languagee == "es":
            tts = gTTS(text=text, lang="es", slow=False)
            fps = 0.41
        else:
            language = detect(text)
            tts = gTTS(text=text, lang=language, slow=True)
            fps = 0.4
    if videoTypeUser == 0:
            # تحويل النص إلى ملف صوتي
        if languagee == "ar":
            tts = gTTS(text=text, lang="ar", slow=False)
            fps = 0.33
        elif languagee == "en":
            tts = gTTS(text=text, lang="en", slow=False)
            fps = 0.33
        elif languagee == "fr":
            tts = gTTS(text=text, lang="fr", slow=False)
            fps = 0.33
        elif languagee == "es":
            tts = gTTS(text=text, lang="es", slow=False)
            fps = 0.33
        else:
            language = detect(text)
            tts = gTTS(text=text, lang=language, slow=False)
            fps = 0.33

    tts.save("assets\\hello.mp3")
    # set up video parameters



    width = 480
    height = 480

    merging_sounds()
    # specify the path to your images
    img_dir = 'images'

    # get a list of all the image file names
    img_files = sorted([f for f in os.listdir(img_dir)])
    # if len(img_files)==0:
    #      img_files = sorted([f for f in os.listdir(img_dir) if f.endswith('.png')])
    if videoTypeUser == 0:


        # with WAVE.open('assets\\mergingSound.mp3', 'rb') as audio_file:
        #     # استرداد معلومات المقطع الصوتي
        #     params = audio_file.getparams()
        #     # استرداد طول المقطع الصوتي بالثواني
        #     duration_in_seconds = float(params[3]) / params[2]
        audio = MP3('assets\\mergingSound.mp3')
        # contains all the metadata about the wavpack file
        audio_info = audio.info
        duration_in_seconds = int(audio_info.length)
        orderPhoto=int(duration_in_seconds /3) 
        while len(img_files) < orderPhoto:
            x=orderPhoto-len(img_files)
            print("x = "  + str(x))
            img_files= img_files+ img_files[0:x]
            print("img_files "+str(len(img_files)))
        print("orderPhoto " +str(orderPhoto))
        print("img_files "+str(len(img_files)))

        
    if videoTypeUser != 0:
        while len(img_files) < len(newText):
            x=len(newText)-len(img_files)
            print("x = "  + str(x))
            img_files= img_files+ img_files[0:x]
            print("img_files "+str(len(img_files)))
        print("newText " +str(len(newText)))
        print("img_files "+str(len(img_files)))
        #print("img_files")
        #print(img_files)


    # create a video writer object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('assets\\output.mp4', fourcc, fps, (width, height))

    # loop over each image and add it to the video
    x=0
    for img_file in img_files:
        # read the image file
        img = cv2.imread(os.path.join(img_dir, img_file))
        # resize the image to fit the video frame
        img = cv2.resize(img, (width, height))
        if videoTypeUser != 0:
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
            font_color = (0, 0, 0)
            thickness = 2
        
            text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
            #text_x = int((width - text_size[1]) / 2)
            text_x = int((width / 2 )- (text_width / 2))#int((img.shape[1] - (text_width / 2)) / 2)
            text_y = img.shape[0] - text_size[1] - 10
            bg_color = (255, 255, 255)  # Green background color
            w = text_width+ 30
            h = text_size[1] + 30
            # Draw the background rectangle
            cv2.rectangle(img, (text_x,text_y-25), (text_x+w , text_y-10 + h), bg_color, -1)
            
            # text_x = int((img.shape[1]) / 2) + int(text_size[0] / 2)
            # text_x = int((img.shape[1] + (text_width / 2)) / 2)
            #cv2.putText(img, text , (text_x, text_y), font, font_scale, font_color, thickness, cv2.LINE_AA)
            # img = put_arabic_text(img, text, (200, 450))
            img = put_arabic_text(img, text, (text_x, 430), font_color)

        # write the image to the video
        out.write(img)
        x+=1

        

    # release the video writer object
    out.release()


    # Load the video and audio clips
    video = VideoFileClip('assets\\output.mp4')
    
    audio = AudioFileClip('assets\\mergingSoundd.mp3')


    # Set the audio clip to the same duration as the video clip
    audio = audio.set_duration(video.duration)

    # Concatenate the video clip and audio clip
    final_clip = video.set_audio(audio)

    # Write the final clip to a new file
    final_clip.write_videofile("output\\"+languagee+".mp4")


