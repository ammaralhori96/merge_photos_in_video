
from googletrans import Translator
import os
from PIL import Image
lang=["ar","en","fr","es"]


titleUser=str(input("Enter title: "))
renameUser=input("rename image files y or n ")
iconUser=input("add icon  y or n ")

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

def addingIconImage():
    path = 'images'
    iconImage = Image.open('assets\\icon480.png')
    # الحصول على قائمة بأسماء جميع الملفات داخل المجلد
    files = os.listdir(path)

    # بدء العدد من 1
    i = 1

    # حلقة تكرارية لإعادة تسمية الملفات
    for file_name in files:
        # الحصول على المسار الكامل للملف
        file_path = os.path.join(path, file_name)
        image1 = Image.open(file_path)
        # قص الصورة الثانية إلى الحجم المطلوب
        image1 = image1.resize((480,480))  # يتم تعيين الحجم بشكل افتراضي هنا

        # الدمج
        image1.paste(iconImage, (0, 0), iconImage)

        # حفظ الصورة الناتجة
        image1.save(file_path)


if renameUser == "y" :
    reanameFilesImage()

if iconUser == "y" :
    addingIconImage()
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
    print(text)
    translator = Translator()
    for i in range(len(lang)):
        translated_text = translator.translate(text, dest=lang[i])
        print(translated_text)
        with open('titleDesc\\'+lang[i]+'.txt', 'w', encoding="utf-8") as filee:

            filee.write(translated_text.text)



os.startfile('titleDesc\\caverTitle.txt')
os.startfile('titleDesc\\youtubeTitle.txt')
os.startfile('images\\')

