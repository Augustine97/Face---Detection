import cv2                                                                                # importing opencv 
  
detect=cv2.CascadeClassifier(r'C:\Users\Augustine\Desktop\Internship\face- detection\face-2\haarcascade_file_face_detection-20191213T100539Z-001\haarcascade_file_face_detection\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)                                                      #switching on the camera
while True:                                  # since we need to capture the vedio continously we run a infinite loop
    ret, img = cap.read()               # array of images are stored on img array and ret returns true if image captured else returns false
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=detect.detectMultiScale(img,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle (img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('camera', img)      # the image is shown
    if cv2.waitKey(1) & 0xff == ord('q'):    # the user is given i sec to press 'q' to disconnect the camera
        break
              
cap.release() 
cv2.destroyAllWindows()   #close all windows

