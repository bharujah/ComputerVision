import cv2

# reading and writing the images......................................................................

#img = cv2.imread("./data/test.png",0) #grayscale -> img = cv2.imread("./data/test.png",cv2.IMREAD_GRAYSCALE)
img = cv2.imread("./data/test.png",1) #normal image

cv2.imshow("output",img)
cv2.imwrite("./data/outputimage.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#image resizing.........................................................................................

print('original dimension', img.shape) # original dimension (991, 1354, 3) 
