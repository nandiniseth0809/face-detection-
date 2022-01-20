import cv2
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
while True:
    ret, frame=cap.read()
    if ret==False:
        continue
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face=face_cascade.detectMultiScale(frame,1.3,5)
    print(face)
    print("i love ice cream")
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        offset=10
        frame = frame[y-offset:y+h+offset,x-offset:x + w+offset]
        frame=cv2.resize(frame,(200,200))

    cv2.imshow('hmm',frame)

    keypressed=cv2.waitKey(1) & 0xFF
    if keypressed==ord('q'):
        break
cap.release()
cap.destroyAllWindows()
