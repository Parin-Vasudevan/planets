import cv2

planets=cv2.imread("solar-system.jpg")

cv2.putText(planets,"sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(0.255,255,255))
cv2.putText(planets,"mercury",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(250,255,255))
cv2.putText(planets,"venus",(200,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(planets,"earth",(270,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,250,255))
cv2.putText(planets,"mars",(380,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(planets,"jupiter",(530,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,250))
cv2.putText(planets,"saturn",(750,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,250))
cv2.putText(planets,"uranus",(970,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(planets,"neptune",(1100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))



cv2.imshow("output",planets)
cv2.waitKey(0)
cv2.imwrite("solar-system-new.jpg",planets)