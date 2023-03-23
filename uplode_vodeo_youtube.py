import pyautogui
import time
from pywinauto.keyboard import send_keys



#2,3,4,2 ترتيب الحسابات والاخير هو العودة للحساب العربي
accountsXY=[(226,563),(224,695),(225,832),(226,563)]
videoXY=[(769,428),(224,695),(225,832),(226,563)]
def opiningApp(broserName):
    
    pyautogui.press("win")
    time.sleep(1)
    send_keys(broserName)
    time.sleep(2)
    pyautogui.press("Enter")
    time.sleep(3)
    send_keys("youtube.com")
    time.sleep(1)
    pyautogui.press("Enter")
    time.sleep(3)



def choosingAccount (xyAcount):
    pyautogui.move(56,123)
    time.sleep(3)
    pyautogui.click(56,123)
    time.sleep(3)
    pyautogui.click(346,368)#accountChanger bouuton
    time.sleep(3)
    pyautogui.click(xyAcount)#account xy
    time.sleep(3)


def uplodeVideo(videoXY):
    time.sleep(1)
    pyautogui.click(190,119)
    time.sleep(1)
    pyautogui.click(285,183) #زر تحميل الفيديو
    time.sleep(4)
    pyautogui.click(918,701) # اختيار الملفات
    time.sleep(1)
    pyautogui.click(1021,275) # مربع المجلد
    time.sleep(1)
    send_keys("C:\\Users\\ammar\\Desktop\\myCodes\\mergePhotos\\output")
    #pyautogui.write("C:\\Users\\ammar\\Desktop\\myCodes\\mergePhotos\\output")
    time.sleep(3)
    pyautogui.press("Enter")
    time.sleep(3)
    pyautogui.doubleClick(videoXY) # اختيار القيديو 
    time.sleep(30)
    pyautogui.click(1200,425)
    time.sleep(1)
    pyautogui.scroll(-200)
    time.sleep(2)
    pyautogui.click(1393,768)
    time.sleep(1)
    pyautogui.click(1021,275) # مربع المجلد
    time.sleep(1)
    send_keys("C:\\Users\\ammar\\Desktop\\myCodes\\mergePhotos\\caverImage")
    #pyautogui.write("C:\\Users\\ammar\\Desktop\\myCodes\\mergePhotos\\caverImage")
    time.sleep(3)
    pyautogui.press("Enter")
    time.sleep(3)
    pyautogui.doubleClick(videoXY) # اختيار الصورة المصغرة 
    time.sleep(1)
    pyautogui.scroll(200)
    time.sleep(2)
    pyautogui.click(1200,450)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(3)
    send_keys('مرحبا بالعالم!')
    time.sleep(3)
    pyautogui.click(1300,600)
    time.sleep(3)
    send_keys('مرحبا بالعالم!')
    time.sleep(1)
    pyautogui.click(373,926) #التالي
    time.sleep(1)
    pyautogui.click(1450,745) #ليس مخصص للاطفال
    time.sleep(1)
    pyautogui.click(373,926) #التالي
    time.sleep(2)
    pyautogui.click(373,926) #التالي
    time.sleep(2)
    pyautogui.click(373,926) #التالي
    time.sleep(2)
    pyautogui.click(1386,678) #علني
    time.sleep(2)
    pyautogui.click(373,926) #نشر
    time.sleep(10)
    pyautogui.click(653,805) #اغلاق
    time.sleep(10)



opiningApp("Edge")
for i in range(len(accountsXY)) :
    uplodeVideo(videoXY[i])
    choosingAccount(accountsXY[i])
    pass