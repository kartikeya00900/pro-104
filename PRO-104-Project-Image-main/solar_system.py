import cv2
import numpy as np

img=cv2.imread("solar-system.jpg")
cv2.imshow("display image",img)

ss=img[120:360,400:500]
img[0:240,500:600]=ss
text_to_show='Sun'
cv2.putText(img,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=5,color=(255,255,255))
            
text_to_show='Mercury'
cv2.putText(img,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=5,color=(255,255,255))            

text_to_show='Venus'
cv2.putText(img,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=5,color=(255,255,255))

text_to_show='Earth'
cv2.putText(img,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=5,color=(255,255,255))

text_to_show='Mars'
cv2.putText(img,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=5,color=(255,255,255))

text_to_show='Jupiter'
cv2.putText(img,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=5,color=(255,255,255))


text_to_show='Saturn'
cv2.putText(img,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=5,color=(255,255,255))


text_to_show='Uranus'
cv2.putText(img,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=5,color=(255,255,255))


text_to_show='Neptune'
cv2.putText(img,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=5,color=(255,255,255))
cv2.waitKey(0)