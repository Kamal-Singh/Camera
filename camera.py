import cv2,sys,os
if getattr(sys, 'frozen', False):
     # if you are running in a |PyInstaller| bundle
     extDataDir = sys._MEIPASS
     extDataDir  = os.path.join(extDataDir, 'haarcascade_frontalface_default.xml') 
     #you should use extDataDir as the path to your file Store_Codes.csv file
else:
     # we are running in a normal Python environment
     extDataDir = os.getcwd()
     extDataDir = os.path.join(extDataDir,'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(extDataDir)
video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,
    scaleFactor=1.1,
    minNeighbors=5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,200,0),2)
    cv2.imshow("Camera",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
video.release()