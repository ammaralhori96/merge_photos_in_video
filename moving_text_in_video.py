
from moviepy.editor import *
from gtts import gTTS

from googletrans import Translator
# النص الذي تريد تحويله إلى صوت

with open('textSp.txt', 'r', encoding="utf-8") as file:
    text = file.read()
    print(text)

# تحويل النص إلى ملف صوتي
tts = gTTS(text=text, lang='en')
tts.save("assets\\hello.mp3")

# اسم الصورة التي ستوضع في الخلفية
background_image_path = "Photo3.jpg"

# اسم الملف الصوتي الذي سيتم تضمينه في الفيديو
audio_path = 'assets\\hello.mp3'

# إنشاء مقطع الفيديو بالحجم والمدة المحددة
clip = ImageClip(background_image_path).set_duration(23)

# إضافة الموسيقى إلى المقطع
clip = clip.set_audio(AudioFileClip(audio_path).set_duration(clip.duration))

# إنشاء نص وتحريكه للأعلى
txt_clip = (TextClip(text, fontsize=30, color='black' , bg_color= "white")
            .set_position('bottom')
            .set_duration(23)
            .set_start(0)
            .set_end(23)
            .set_position(lambda t: ('center', 100-t*20))
            )

# إضافة نص للمقطع
video = CompositeVideoClip([clip, txt_clip])

# حفظ المقطع المصمم كفيديو
video.write_videofile("output\\my_video.mp4", fps=24)

