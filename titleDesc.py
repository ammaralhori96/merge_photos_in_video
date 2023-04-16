
from googletrans import Translator
import os
lang=["ar","en","fr","es"]


titleUser=str(input("Enter title: "))
renameUser=input("rename image files y or n ")

def reanameFilesImage():
    path = 'images'
    # الحصول على قائمة بأسماء جميع الملفات داخل المجلد
    files = os.listdir(path)

    # بدء العدد من 1
    i = 1

    # حلقة تكرارية لإعادة تسمية الملفات
    for file_name in files:
        # الحصول على المسار الكامل للملف
        file_path = os.path.join(path, file_name)
        
        # إعادة تسمية الملف باستخدام رقم فريد
        new_file_name = str(i) + ".jpg"
        new_file_path = os.path.join(path, new_file_name)
        os.rename(file_path, new_file_path)
        
        # زيادة العدد بمقدار واحد
        i += 1
    os.startfile('images')

if renameUser == "y" :
    reanameFilesImage()
#############title################### 
translator = Translator()
for i in range(len(lang)):
    translated_text = translator.translate(titleUser, dest=lang[i])
    if i == 0 :
        with open('titleDesc\\caverTitle.txt', 'w', encoding="utf-8") as filee:

            filee.write(translated_text.text)
            filee.write("\n")
        with open('titleDesc\\youtubeTitle.txt', 'w', encoding="utf-8") as filee:

            filee.write(translated_text.text)
            filee.write("\n")
    else:
        with open('titleDesc\\caverTitle.txt', 'a', encoding="utf-8") as filee:

            filee.write(translated_text.text)
            filee.write("\n")
        with open('titleDesc\\youtubeTitle.txt', 'a', encoding="utf-8") as filee:

            filee.write(translated_text.text)
            filee.write("\n")
    

#############Discriotion###################        
with open('textSp.txt', 'r', encoding="utf-8") as file:
    text=file.read()
    #text = text.replace("\n", " " )

    translator = Translator()
    for i in range(len(lang)):
        translated_text = translator.translate(text, dest=lang[i])

        with open('titleDesc\\'+lang[i]+'.txt', 'w', encoding="utf-8") as filee:

            filee.write(translated_text.text)



os.startfile('titleDesc\\caverTitle.txt')
os.startfile('titleDesc\\youtubeTitle.txt')
os.startfile('images\\')

