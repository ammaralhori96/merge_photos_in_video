
import cv2

#print("ttttttt")
# افتح الفيديو المصدر
videoFolder='videos\\video.mp4'
outputFolder='output\\video.mp4'
imgPos='assets\\sindibadIcon.png'
cap = cv2.VideoCapture(videoFolder)

# قراءة الصورة PNG
overlay = cv2.imread(imgPos, cv2.IMREAD_UNCHANGED)

# حجم الفيديو
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# إعداد الفيديو المعدل
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(outputFolder, fourcc, 25.0, (frame_width, frame_height))

# حلق على الفيديو ووضع الصورة فوق كل إطار
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # وضع الصورة فوق الإطار
    x_offset = 10
    y_offset = 10
    alpha_s = overlay[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s
    for c in range(0, 3):
        frame[y_offset:y_offset+overlay.shape[0], x_offset:x_offset+overlay.shape[1], c] = (
            alpha_s * overlay[:, :, c] + alpha_l * frame[y_offset:y_offset+overlay.shape[0], x_offset:x_offset+overlay.shape[1], c]
        )

    # كتابة الإطار المعدل إلى الفيديو المعدل
    out.write(frame)

# تنظيف المصادر
cap.release()
out.release()
cv2.destroyAllWindows()

