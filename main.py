import cv2
import numpy as np
import json

INPUT_IMG_1 = 'im1.jpg'
INPUT_IMG_2 = 'im2.jpg'
OUTPUT_JSON_FILE = 'file.json'

def rec_click1(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print 'hello-click1 ', event, x, y
        cv2.circle( im1, (x,y), 10, (0,0,255), -1 )
        clicks1.append( (x,y) )

def rec_click2(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print 'hello-click2 ', event, x, y
        cv2.circle( im2, (x,y), 10, (0,255,255), -1 )
        clicks2.append( (x,y) )


# Load 1st Image
im1 = cv2.imread( INPUT_IMG_1 )
cv2.namedWindow( INPUT_IMG_1)
cv2.setMouseCallback(INPUT_IMG_1, rec_click1 )
clicks1 = []

# Load 2nd Image
im2 = cv2.imread( INPUT_IMG_2 )
cv2.namedWindow( INPUT_IMG_2)
cv2.setMouseCallback(INPUT_IMG_2, rec_click2 )
clicks2 = []

# Event Loop
print 'press c to quit'
while True:
    key = cv2.waitKey(20) & 0xFF
    cv2.imshow( INPUT_IMG_1, im1 )
    cv2.imshow( INPUT_IMG_2, im2 )
    if  key == ord('c'):
        break

# Write Json
f = {}
f['im1_clicks'] = clicks1
f['im2_clicks'] = clicks2
fp = open( 'file.json', 'w' )
fp.write( json.dumps( f, indent=4  ) )
fp.close()
