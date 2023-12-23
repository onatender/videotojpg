import cv2
import os


video_path = input("Video dosyasının yolunu girin: ")


cap = cv2.VideoCapture(video_path)


if not cap.isOpened():
    print("Video dosyası açılamadı.")
    exit()


output_folder = "video_frames"
os.makedirs(output_folder, exist_ok=True)


frame_number = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_number += 1
    frame_filename = os.path.join(output_folder, f"{frame_number}.jpg")
    

    cv2.imwrite(frame_filename, frame)
    
    print(f"{frame_filename} kaydedildi.")


cap.release()
cv2.destroyAllWindows()

print("Tüm çerçeveler başarıyla kaydedildi.")
