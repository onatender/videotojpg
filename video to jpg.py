import cv2
import os

# Kullanıcıdan video dosyasının yolunu alın
video_path = input("Video dosyasının yolunu girin: ")

# Video dosyasını açın
cap = cv2.VideoCapture(video_path)

# Video dosyasının varlığını kontrol edin
if not cap.isOpened():
    print("Video dosyası açılamadı.")
    exit()

# Klasör oluşturun
output_folder = "video_frames"
os.makedirs(output_folder, exist_ok=True)

# Kareden kareye ilerleyerek videodan çerçeveleri kaydedin
frame_number = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_number += 1
    frame_filename = os.path.join(output_folder, f"{frame_number}.jpg")
    
    # Çerçeveyi kaydet
    cv2.imwrite(frame_filename, frame)
    
    print(f"{frame_filename} kaydedildi.")

# Temizlik yapın ve kaynakları serbest bırakın
cap.release()
cv2.destroyAllWindows()

print("Tüm çerçeveler başarıyla kaydedildi.")
