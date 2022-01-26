import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Ensure frame width and height match the output
fw = int(cap.get(3))
fh = int(cap.get(4))
out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('X','V','I','D'), 30, (fw,fh))


while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

out.release()

cv2.destroyAllWindows()