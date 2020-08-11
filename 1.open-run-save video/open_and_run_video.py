#pip install opencv-python

#video oynatma
import cv2
cap = cv2.VideoCapture('../input/yawning.avi') # vtest.avi adında video dosyasını acıyoruz
while(cap.isOpened()): #ve cap isimli değişken açık olana kadar yani video dosyası açık olduğu sürece
    ret, frame = cap.read() # gelen veriyi anlık okuyoruz
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # COLOR_BGR2GRAY modunda dönüştürdük
    cv2.imshow('frame',gray) # pencere ismini ve gösterilecek olan veriyi yazdık ve ekranda görüntü aldık 
    if cv2.waitKey(1) & 0xFF == ord('q'): #klavye ile kapatma işlemlerini ekledik,klavye ile döngüyü yani veri okunmasını durdurmak için
        break
cap.release()
cv2.destroyAllWindows() # pencereleri yok ettik
