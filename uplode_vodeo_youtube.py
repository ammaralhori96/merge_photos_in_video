from gtts import gTTS

from googletrans import Translator
# النص الذي تريد تحويله إلى صوت

with open('textSp.txt', 'r', encoding="utf-8") as file:
    text = file.read()
    print(text)

# تحويل النص إلى ملف صوتي
tts = gTTS(text=text, lang='ar')
tts.save("assets\\hello.mp3")





translator = Translator(service_urls=['translate.google.com'])
text_to_translate = "مرحبا بك"
translation = translator.translate(text_to_translate, dest='en')
print(translation.text)
