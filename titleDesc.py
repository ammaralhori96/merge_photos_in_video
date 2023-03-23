
from googletrans import Translator

lang=["ar","en","fr","es"]


titleUser=input("Enter title: ")

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
with open('titleDesc\\textSp.txt', 'r', encoding="utf-8") as file:
    text=file.read()
    #text = text.replace("\n", " " )

    translator = Translator()
    for i in range(len(lang)):
        translated_text = translator.translate(text, dest=lang[i])

        with open('titleDesc\\'+lang[i]+'.txt', 'w', encoding="utf-8") as filee:

            filee.write(translated_text.text)


