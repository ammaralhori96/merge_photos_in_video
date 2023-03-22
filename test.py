import cv2

# فتح ملف الفيديو
cap = cv2.VideoCapture('video_with_sound.mp4')

# إنشاء متغير لتحديد الخط وحجم الخط
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255, 255, 255)
thickness = 2

# إنشاء متغير لتحديد إعدادات الفيديو الجديد
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('outputt.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (width,height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # إضافة النص على الفيديو
        cv2.putText(frame, 'Hello World!', (50, 50), font, fontScale, fontColor, thickness, cv2.LINE_AA)
        
        # عرض الفيديو المعدل
        out.write(frame)
        cv2.imshow('frame', frame)
        
        # الخروج إذا تم الضغط على زر q
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# إغلاق الفيديو
cap.release()
out.release()
cv2.destroyAllWindows()
